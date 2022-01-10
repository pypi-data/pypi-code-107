#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

import atexit
import copy
import datetime
import functools
import operator
import signal
import threading
import types
import uuid

from neutron_lib.api.definitions import portbindings
from neutron_lib.api.definitions import provider_net
from neutron_lib.api.definitions import segment as segment_def
from neutron_lib.callbacks import events
from neutron_lib.callbacks import registry
from neutron_lib.callbacks import resources
from neutron_lib import constants as const
from neutron_lib import context as n_context
from neutron_lib import exceptions as n_exc
from neutron_lib.exceptions import availability_zone as az_exc
from neutron_lib.plugins import directory
from neutron_lib.plugins.ml2 import api
from oslo_concurrency import processutils
from oslo_config import cfg
from oslo_db import exception as os_db_exc
from oslo_log import log
from oslo_utils import timeutils
from ovsdbapp.backend.ovs_idl import idlutils

from neutron._i18n import _
from neutron.common.ovn import acl as ovn_acl
from neutron.common.ovn import constants as ovn_const
from neutron.common.ovn import extensions as ovn_extensions
from neutron.common.ovn import utils as ovn_utils
from neutron.conf.plugins.ml2.drivers.ovn import ovn_conf
from neutron.db import ovn_hash_ring_db
from neutron.db import ovn_revision_numbers_db
from neutron.db import provisioning_blocks
from neutron.extensions import securitygroup as ext_sg
from neutron.plugins.ml2 import db as ml2_db
from neutron.plugins.ml2.drivers.ovn.agent import neutron_agent as n_agent
from neutron.plugins.ml2.drivers.ovn.mech_driver.ovsdb import impl_idl_ovn
from neutron.plugins.ml2.drivers.ovn.mech_driver.ovsdb import maintenance
from neutron.plugins.ml2.drivers.ovn.mech_driver.ovsdb import ovn_client
from neutron.plugins.ml2.drivers.ovn.mech_driver.ovsdb import ovn_db_sync
from neutron.plugins.ml2.drivers.ovn.mech_driver.ovsdb import ovsdb_monitor
from neutron.plugins.ml2.drivers.ovn.mech_driver.ovsdb import worker
from neutron import service
from neutron.services.logapi.drivers.ovn import driver as log_driver
from neutron.services.qos.drivers.ovn import driver as qos_driver
from neutron.services.segments import db as segment_service_db
from neutron.services.trunk.drivers.ovn import trunk_driver
import neutron.wsgi


LOG = log.getLogger(__name__)
OVN_MIN_GENEVE_MAX_HEADER_SIZE = 38


class OVNPortUpdateError(n_exc.BadRequest):
    pass


class OVNMechanismDriver(api.MechanismDriver):
    """OVN ML2 mechanism driver

    A mechanism driver is called on the creation, update, and deletion
    of networks and ports. For every event, there are two methods that
    get called - one within the database transaction (method suffix of
    _precommit), one right afterwards (method suffix of _postcommit).

    Exceptions raised by methods called inside the transaction can
    rollback, but should not make any blocking calls (for example,
    REST requests to an outside controller). Methods called after
    transaction commits can make blocking external calls, though these
    will block the entire process. Exceptions raised in calls after
    the transaction commits may cause the associated resource to be
    deleted.

    Because rollback outside of the transaction is not done in the
    update network/port case, all data validation must be done within
    methods that are part of the database transaction.
    """
    resource_provider_uuid5_namespace = uuid.UUID(
        '5533233b-800c-11eb-b1f4-000056b2f5b8')

    def initialize(self):
        """Perform driver initialization.

        Called after all drivers have been loaded and the database has
        been initialized. No abstract methods defined below will be
        called prior to this method being called.
        """
        LOG.info("Starting OVNMechanismDriver")
        self._nb_ovn = None
        self._sb_ovn = None
        self._plugin_property = None
        self._ovn_client_inst = None
        self._maintenance_thread = None
        self.node_uuid = None
        self.hash_ring_group = ovn_const.HASH_RING_ML2_GROUP
        self.sg_enabled = ovn_acl.is_sg_enabled()
        # NOTE(lucasagomes): _clean_hash_ring() must be called before
        # self.subscribe() to avoid processes racing when adding or
        # deleting nodes from the Hash Ring during service initialization
        self._clean_hash_ring()
        self._post_fork_event = threading.Event()
        if cfg.CONF.SECURITYGROUP.firewall_driver:
            LOG.warning('Firewall driver configuration is ignored')
        if (const.TYPE_GENEVE in cfg.CONF.ml2.type_drivers and
                cfg.CONF.ml2_type_geneve.max_header_size <
                OVN_MIN_GENEVE_MAX_HEADER_SIZE):
            LOG.critical('Geneve max_header_size set too low for OVN '
                         '(%d vs %d)',
                      cfg.CONF.ml2_type_geneve.max_header_size,
                      OVN_MIN_GENEVE_MAX_HEADER_SIZE)
            raise SystemExit(1)
        self._setup_vif_port_bindings()
        if impl_idl_ovn.OvsdbSbOvnIdl.schema_has_table('Chassis_Private'):
            self.agent_chassis_table = 'Chassis_Private'
        else:
            self.agent_chassis_table = 'Chassis'
        self.subscribe()
        self.qos_driver = qos_driver.OVNQosDriver.create(self)
        self.trunk_driver = trunk_driver.OVNTrunkDriver.create(self)
        self.log_driver = log_driver.register(self)

    @property
    def nb_schema_helper(self):
        return impl_idl_ovn.OvsdbNbOvnIdl.schema_helper

    @property
    def sb_schema_helper(self):
        return impl_idl_ovn.OvsdbSbOvnIdl.schema_helper

    @property
    def _plugin(self):
        if self._plugin_property is None:
            self._plugin_property = directory.get_plugin()
        return self._plugin_property

    @property
    def _ovn_client(self):
        if self._ovn_client_inst is None:
            self._ovn_client_inst = ovn_client.OVNClient(self.nb_ovn,
                                                         self.sb_ovn)
        return self._ovn_client_inst

    @property
    def nb_ovn(self):
        self._post_fork_event.wait()
        return self._nb_ovn

    @nb_ovn.setter
    def nb_ovn(self, val):
        self._nb_ovn = val

    @property
    def sb_ovn(self):
        self._post_fork_event.wait()
        return self._sb_ovn

    @sb_ovn.setter
    def sb_ovn(self, val):
        self._sb_ovn = val

    def check_vlan_transparency(self, context):
        """OVN driver vlan transparency support."""
        vlan_transparency_network_types = [
            const.TYPE_LOCAL,
            const.TYPE_GENEVE,
            const.TYPE_VXLAN,
            const.TYPE_VLAN
        ]
        return (context.current.get(provider_net.NETWORK_TYPE)
                in vlan_transparency_network_types)

    def _setup_vif_port_bindings(self):
        self.supported_vnic_types = [portbindings.VNIC_NORMAL,
                                     portbindings.VNIC_DIRECT,
                                     portbindings.VNIC_DIRECT_PHYSICAL,
                                     portbindings.VNIC_MACVTAP,
                                     portbindings.VNIC_VHOST_VDPA,
                                     ]
        self.vif_details = {
            portbindings.VIF_TYPE_OVS: {
                portbindings.CAP_PORT_FILTER: self.sg_enabled
            },
            portbindings.VIF_TYPE_VHOST_USER: {
                portbindings.CAP_PORT_FILTER: False,
                portbindings.VHOST_USER_MODE:
                portbindings.VHOST_USER_MODE_SERVER,
                portbindings.VHOST_USER_OVS_PLUG: True
            },
            portbindings.VIF_DETAILS_CONNECTIVITY:
                portbindings.CONNECTIVITY_L2,
        }

    def supported_extensions(self, extensions):
        return set(ovn_extensions.ML2_SUPPORTED_API_EXTENSIONS) & extensions

    def subscribe(self):
        registry.subscribe(self.pre_fork_initialize,
                           resources.PROCESS,
                           events.BEFORE_SPAWN)
        registry.subscribe(self.post_fork_initialize,
                           resources.PROCESS,
                           events.AFTER_INIT)
        registry.subscribe(self._add_segment_host_mapping_for_segment,
                           resources.SEGMENT,
                           events.AFTER_CREATE)
        registry.subscribe(self.create_segment_provnet_port,
                           resources.SEGMENT,
                           events.AFTER_CREATE)
        registry.subscribe(self.delete_segment_provnet_port,
                           resources.SEGMENT,
                           events.AFTER_DELETE)

        # Handle security group/rule notifications
        if self.sg_enabled:
            registry.subscribe(self._create_security_group_precommit,
                               resources.SECURITY_GROUP,
                               events.PRECOMMIT_CREATE)
            registry.subscribe(self._update_security_group,
                               resources.SECURITY_GROUP,
                               events.AFTER_UPDATE)
            registry.subscribe(self._create_security_group,
                               resources.SECURITY_GROUP,
                               events.AFTER_CREATE)
            registry.subscribe(self._delete_security_group,
                               resources.SECURITY_GROUP,
                               events.AFTER_DELETE)
            registry.subscribe(self._create_sg_rule_precommit,
                               resources.SECURITY_GROUP_RULE,
                               events.PRECOMMIT_CREATE)
            registry.subscribe(self._process_sg_rule_notification,
                               resources.SECURITY_GROUP_RULE,
                               events.AFTER_CREATE)
            registry.subscribe(self._process_sg_rule_notification,
                               resources.SECURITY_GROUP_RULE,
                               events.BEFORE_DELETE)

    def _clean_hash_ring(self, *args, **kwargs):
        admin_context = n_context.get_admin_context()
        ovn_hash_ring_db.remove_nodes_from_host(admin_context,
                                                self.hash_ring_group)

    def pre_fork_initialize(self, resource, event, trigger, payload=None):
        """Pre-initialize the ML2/OVN driver."""
        atexit.register(self._clean_hash_ring)
        signal.signal(signal.SIGTERM, self._clean_hash_ring)
        self._create_neutron_pg_drop()
        self._set_inactivity_probe()

    def _create_neutron_pg_drop(self):
        """Create neutron_pg_drop Port Group.

        The method creates a short living connection to the Northbound
        database. Because of multiple controllers can attempt to create the
        Port Group at the same time the transaction can fail and raise
        RuntimeError. In such case, we make sure the Port Group was created,
        otherwise the error is something else and it's raised to the caller.
        """
        idl = ovsdb_monitor.OvnInitPGNbIdl.from_server(
            ovn_conf.get_ovn_nb_connection(), self.nb_schema_helper, self)
        # Only one server should try to create the port group
        idl.set_lock('pg_drop_creation')
        with ovsdb_monitor.short_living_ovsdb_api(
                impl_idl_ovn.OvsdbNbOvnIdl, idl) as pre_ovn_nb_api:
            try:
                create_default_drop_port_group(pre_ovn_nb_api)
            except KeyError:
                # Due to a bug in python-ovs, we can send transactions before
                # the initial OVSDB is populated in memory. This can break
                # the AddCommand post_commit method which tries to return a
                # row looked up by the newly commited row's uuid. Since we
                # don't care about the return value from the PgAddCommand, we
                # can just catch the KeyError and continue. This can be
                # removed when the python-ovs bug is resolved.
                pass
            except RuntimeError as re:
                # If we don't get the lock, and the port group didn't exist
                # when we tried to create it, it might still have been
                # created by another server and we just haven't gotten the
                # update yet.
                LOG.info("Waiting for Port Group %(pg)s to be created",
                         {'pg': ovn_const.OVN_DROP_PORT_GROUP_NAME})
                if not idl.neutron_pg_drop_event.wait():
                    LOG.error("Port Group %(pg)s was not created in time",
                              {'pg': ovn_const.OVN_DROP_PORT_GROUP_NAME})
                    raise re
                LOG.info("Porg Group %(pg)s was created by another server",
                         {'pg': ovn_const.OVN_DROP_PORT_GROUP_NAME})

    def _set_inactivity_probe(self):
        """Set 'connection.inactivity_probe' in NB and SB databases"""
        inactivity_probe = ovn_conf.get_ovn_ovsdb_probe_interval()
        dbs = [(ovn_conf.get_ovn_nb_connection(), self.nb_schema_helper,
                impl_idl_ovn.OvsdbNbOvnIdl),
               (ovn_conf.get_ovn_sb_connection(), self.sb_schema_helper,
                impl_idl_ovn.OvsdbSbOvnIdl)]
        for connection, schema, klass in dbs:
            target = ovn_utils.connection_config_to_target_string(connection)
            if not target:
                continue

            idl = ovsdb_monitor.BaseOvnIdl.from_server(connection, schema)
            with ovsdb_monitor.short_living_ovsdb_api(klass, idl) as idl_api:
                conn = idlutils.row_by_value(idl_api, 'Connection', 'target',
                                             target, None)
                if conn:
                    idl_api.db_set(
                        'Connection', target,
                        ('inactivity_probe', int(inactivity_probe))).execute(
                        check_error=True)

    @staticmethod
    def should_post_fork_initialize(worker_class):
        return worker_class in (neutron.wsgi.WorkerService,
                                worker.MaintenanceWorker,
                                service.RpcWorker)

    def post_fork_initialize(self, resource, event, trigger, payload=None):
        # Initialize API/Maintenance workers with OVN IDL connections
        worker_class = ovn_utils.get_method_class(trigger)
        if not self.should_post_fork_initialize(worker_class):
            return

        self._post_fork_event.clear()
        self._ovn_client_inst = None

        if worker_class == neutron.wsgi.WorkerService:
            admin_context = n_context.get_admin_context()
            self.node_uuid = ovn_hash_ring_db.add_node(admin_context,
                                                       self.hash_ring_group)

        n_agent.AgentCache(self)  # Initialize singleton agent cache
        self.nb_ovn, self.sb_ovn = impl_idl_ovn.get_ovn_idls(self, trigger)

        # Override agents API methods
        self.patch_plugin_merge("get_agents", get_agents)
        self.patch_plugin_choose("get_agent", get_agent)
        self.patch_plugin_choose("update_agent", update_agent)
        self.patch_plugin_choose("delete_agent", delete_agent)

        # Override availability zone methods
        self.patch_plugin_merge("get_availability_zones",
                                get_availability_zones)
        self.patch_plugin_choose("validate_availability_zones",
                                 validate_availability_zones)

        # Now IDL connections can be safely used.
        self._post_fork_event.set()

        if worker_class == worker.MaintenanceWorker:
            # Call the synchronization task if its maintenance worker
            # This sync neutron DB to OVN-NB DB only in inconsistent states
            self.nb_synchronizer = ovn_db_sync.OvnNbSynchronizer(
                self._plugin,
                self.nb_ovn,
                self.sb_ovn,
                ovn_conf.get_ovn_neutron_sync_mode(),
                self
            )
            self.nb_synchronizer.sync()

            # This sync neutron DB to OVN-SB DB only in inconsistent states
            self.sb_synchronizer = ovn_db_sync.OvnSbSynchronizer(
                self._plugin,
                self.sb_ovn,
                self
            )
            self.sb_synchronizer.sync()

            self._maintenance_thread = maintenance.MaintenanceThread()
            self._maintenance_thread.add_periodics(
                maintenance.DBInconsistenciesPeriodics(self._ovn_client))
            self._maintenance_thread.add_periodics(
                maintenance.HashRingHealthCheckPeriodics(
                    self.hash_ring_group))
            self._maintenance_thread.start()

    def _create_security_group_precommit(self, resource, event, trigger,
                                         payload):
        context = payload.context
        security_group = payload.latest_state
        ovn_revision_numbers_db.create_initial_revision(
            context, security_group['id'],
            ovn_const.TYPE_SECURITY_GROUPS,
            std_attr_id=security_group['standard_attr_id'])

    def _create_security_group(self, resource, event, trigger, payload):
        context = payload.context
        security_group = payload.latest_state
        self._ovn_client.create_security_group(context,
                                               security_group)

    def _delete_security_group(self, resource, event, trigger, payload):
        context = payload.context
        security_group_id = payload.resource_id
        self._ovn_client.delete_security_group(context,
                                               security_group_id)

    def _update_security_group(self, resource, event, trigger, payload):
        context = payload.context
        security_group = payload.latest_state

        old_state, new_state = payload.states
        is_allow_stateless_supported = (
            self._ovn_client.is_allow_stateless_supported()
        )
        old_stateful = ovn_acl.is_sg_stateful(
            old_state, is_allow_stateless_supported)
        new_stateful = ovn_acl.is_sg_stateful(
            new_state, is_allow_stateless_supported)
        if old_stateful != new_stateful:
            for rule in self._plugin.get_security_group_rules(
                    context, {'security_group_id': [security_group['id']]}):
                self._ovn_client.delete_security_group_rule(context, rule)
                self._ovn_client.create_security_group_rule(context, rule)

        ovn_revision_numbers_db.bump_revision(
            context, security_group, ovn_const.TYPE_SECURITY_GROUPS)

    def _create_sg_rule_precommit(self, resource, event, trigger,
                                  payload):
        sg_rule = payload.latest_state
        context = payload.context
        ovn_revision_numbers_db.create_initial_revision(
            context, sg_rule['id'], ovn_const.TYPE_SECURITY_GROUP_RULES,
            std_attr_id=sg_rule['standard_attr_id'])

    def _process_sg_rule_notification(
            self, resource, event, trigger, payload):
        context = payload.context
        security_group_rule = payload.latest_state
        security_group_rule_id = payload.resource_id
        if event == events.AFTER_CREATE:
            self._ovn_client.create_security_group_rule(
                context, security_group_rule)
        elif event == events.BEFORE_DELETE:
            try:
                sg_rule = self._plugin.get_security_group_rule(
                    context, security_group_rule_id)
            except ext_sg.SecurityGroupRuleNotFound:
                return

            if sg_rule.get('remote_ip_prefix') is not None:
                if self._sg_has_rules_with_same_normalized_cidr(sg_rule):
                    return
            self._ovn_client.delete_security_group_rule(
                context,
                sg_rule)

    def _sg_has_rules_with_same_normalized_cidr(self, sg_rule):
        compare_keys = [
            'ethertype', 'direction', 'protocol',
            'port_range_min', 'port_range_max']
        sg_rules = self._plugin.get_security_group_rules(
            n_context.get_admin_context(),
            {'security_group_id': [sg_rule['security_group_id']]})

        def _rules_equal(rule1, rule2):
            return not any(
                rule1.get(key) != rule2.get(key) for key in compare_keys)

        for rule in sg_rules:
            if not rule.get('remote_ip_prefix') or rule['id'] == sg_rule['id']:
                continue
            if sg_rule.get('normalized_cidr') != rule.get('normalized_cidr'):
                continue
            if _rules_equal(sg_rule, rule):
                return True
        return False

    def _is_network_type_supported(self, network_type):
        return (network_type in [const.TYPE_LOCAL,
                                 const.TYPE_FLAT,
                                 const.TYPE_GENEVE,
                                 const.TYPE_VXLAN,
                                 const.TYPE_VLAN])

    def _get_max_tunid(self):
        try:
            return int(self.nb_ovn.nb_global.options.get('max_tunid'))
        except (ValueError, TypeError):
            # max_tunid may be absent in older OVN versions, return None
            pass

    def _validate_network_segments(self, network_segments):
        max_tunid = self._get_max_tunid()
        for network_segment in network_segments:
            network_type = network_segment['network_type']
            segmentation_id = network_segment['segmentation_id']
            physical_network = network_segment['physical_network']
            LOG.debug('Validating network segment with '
                      'type %(network_type)s, '
                      'segmentation ID %(segmentation_id)s, '
                      'physical network %(physical_network)s',
                      {'network_type': network_type,
                       'segmentation_id': segmentation_id,
                       'physical_network': physical_network})
            if not self._is_network_type_supported(network_type):
                msg = _('Network type %s is not supported') % network_type
                raise n_exc.InvalidInput(error_message=msg)
            if segmentation_id and max_tunid and segmentation_id > max_tunid:
                m = (
                    _('Segmentation ID should be lower or equal to %d') %
                    max_tunid
                )
                raise n_exc.InvalidInput(error_message=m)

    def create_segment_provnet_port(self, resource, event, trigger,
                                    payload=None):
        segment = payload.latest_state
        if not segment.get(segment_def.PHYSICAL_NETWORK):
            return
        self._ovn_client.create_provnet_port(segment['network_id'], segment)

    def delete_segment_provnet_port(self, resource, event, trigger,
                                    payload):
        # NOTE(mjozefcz): Get the last state of segment resource.
        segment = payload.states[-1]
        if segment.get(segment_def.PHYSICAL_NETWORK):
            self._ovn_client.delete_provnet_port(
                segment['network_id'], segment)

    def create_network_precommit(self, context):
        """Allocate resources for a new network.

        :param context: NetworkContext instance describing the new
        network.

        Create a new network, allocating resources as necessary in the
        database. Called inside transaction context on session. Call
        cannot block.  Raising an exception will result in a rollback
        of the current transaction.
        """
        self._validate_network_segments(context.network_segments)
        ovn_revision_numbers_db.create_initial_revision(
            context._plugin_context, context.current['id'],
            ovn_const.TYPE_NETWORKS,
            std_attr_id=context.current['standard_attr_id'])

    def create_network_postcommit(self, context):
        """Create a network.

        :param context: NetworkContext instance describing the new
        network.

        Called after the transaction commits. Call can block, though
        will block the entire process so care should be taken to not
        drastically affect performance. Raising an exception will
        cause the deletion of the resource.
        """
        network = context.current
        self._ovn_client.create_network(context._plugin_context, network)

    def update_network_precommit(self, context):
        """Update resources of a network.

        :param context: NetworkContext instance describing the new
        state of the network, as well as the original state prior
        to the update_network call.

        Update values of a network, updating the associated resources
        in the database. Called inside transaction context on session.
        Raising an exception will result in rollback of the
        transaction.

        update_network_precommit is called for all changes to the
        network state. It is up to the mechanism driver to ignore
        state or state changes that it does not know or care about.
        """
        self._validate_network_segments(context.network_segments)

    def update_network_postcommit(self, context):
        """Update a network.

        :param context: NetworkContext instance describing the new
        state of the network, as well as the original state prior
        to the update_network call.

        Called after the transaction commits. Call can block, though
        will block the entire process so care should be taken to not
        drastically affect performance. Raising an exception will
        cause the deletion of the resource.

        update_network_postcommit is called for all changes to the
        network state.  It is up to the mechanism driver to ignore
        state or state changes that it does not know or care about.
        """
        # FIXME(lucasagomes): We can delete this conditional after
        # https://bugs.launchpad.net/neutron/+bug/1739798 is fixed.
        if context._plugin_context.session.is_active:
            return
        self._ovn_client.update_network(
            context._plugin_context, context.current,
            original_network=context.original)

    def delete_network_postcommit(self, context):
        """Delete a network.

        :param context: NetworkContext instance describing the current
        state of the network, prior to the call to delete it.

        Called after the transaction commits. Call can block, though
        will block the entire process so care should be taken to not
        drastically affect performance. Runtime errors are not
        expected, and will not prevent the resource from being
        deleted.
        """
        self._ovn_client.delete_network(
            context._plugin_context,
            context.current['id'])

    def create_subnet_precommit(self, context):
        ovn_revision_numbers_db.create_initial_revision(
            context._plugin_context, context.current['id'],
            ovn_const.TYPE_SUBNETS,
            std_attr_id=context.current['standard_attr_id'])

    def create_subnet_postcommit(self, context):
        self._ovn_client.create_subnet(context._plugin_context,
                                       context.current,
                                       context.network.current)

    def update_subnet_postcommit(self, context):
        self._ovn_client.update_subnet(
            context._plugin_context, context.current, context.network.current)

    def delete_subnet_postcommit(self, context):
        self._ovn_client.delete_subnet(context._plugin_context,
                                       context.current['id'])

    def _validate_port_extra_dhcp_opts(self, port):
        result = ovn_utils.validate_port_extra_dhcp_opts(port)
        if not result.failed:
            return
        ipv4_opts = ', '.join(result.invalid_ipv4)
        ipv6_opts = ', '.join(result.invalid_ipv6)
        LOG.info('The following extra DHCP options for port %(port_id)s '
                 'are not supported by OVN. IPv4: "%(ipv4_opts)s" and '
                 'IPv6: "%(ipv6_opts)s"', {'port_id': port['id'],
                 'ipv4_opts': ipv4_opts, 'ipv6_opts': ipv6_opts})

    def create_port_precommit(self, context):
        """Allocate resources for a new port.

        :param context: PortContext instance describing the port.

        Create a new port, allocating resources as necessary in the
        database. Called inside transaction context on session. Call
        cannot block.  Raising an exception will result in a rollback
        of the current transaction.
        """
        port = context.current
        if ovn_utils.is_lsp_ignored(port):
            return
        ovn_utils.validate_and_get_data_from_binding_profile(port)
        self._validate_port_extra_dhcp_opts(port)
        if self._is_port_provisioning_required(port, context.host):
            self._insert_port_provisioning_block(context._plugin_context,
                                                 port['id'])

        ovn_revision_numbers_db.create_initial_revision(
            context._plugin_context, port['id'], ovn_const.TYPE_PORTS,
            std_attr_id=context.current['standard_attr_id'])

        # in the case of router ports we also need to
        # track the creation and update of the LRP OVN objects
        if ovn_utils.is_lsp_router_port(port):
            ovn_revision_numbers_db.create_initial_revision(
                context._plugin_context, port['id'],
                ovn_const.TYPE_ROUTER_PORTS,
                std_attr_id=context.current['standard_attr_id'])

    def _is_port_provisioning_required(self, port, host, original_host=None):
        vnic_type = port.get(portbindings.VNIC_TYPE, portbindings.VNIC_NORMAL)
        if vnic_type not in self.supported_vnic_types:
            LOG.debug('No provisioning block for port %(port_id)s due to '
                      'unsupported vnic_type: %(vnic_type)s',
                      {'port_id': port['id'], 'vnic_type': vnic_type})
            return False

        if port['status'] == const.PORT_STATUS_ACTIVE:
            LOG.debug('No provisioning block for port %s since it is active',
                      port['id'])
            return False

        if not host:
            LOG.debug('No provisioning block for port %s since it does not '
                      'have a host', port['id'])
            return False

        if host == original_host:
            LOG.debug('No provisioning block for port %s since host unchanged',
                      port['id'])
            return False

        if not self.sb_ovn.chassis_exists(host):
            LOG.debug('No provisioning block for port %(port_id)s since no '
                      'OVN chassis for host: %(host)s',
                      {'port_id': port['id'], 'host': host})
            return False

        return True

    def _insert_port_provisioning_block(self, context, port_id):
        # Insert a provisioning block to prevent the port from
        # transitioning to active until OVN reports back that
        # the port is up.
        provisioning_blocks.add_provisioning_component(
            context, port_id, resources.PORT,
            provisioning_blocks.L2_AGENT_ENTITY
        )

    def _notify_dhcp_updated(self, port_id):
        """Notifies Neutron that the DHCP has been update for port."""
        admin_context = n_context.get_admin_context()
        if provisioning_blocks.is_object_blocked(
                admin_context, port_id, resources.PORT):
            provisioning_blocks.provisioning_complete(
                admin_context, port_id, resources.PORT,
                provisioning_blocks.DHCP_ENTITY)

    def _validate_ignored_port(self, port, original_port):
        if ovn_utils.is_lsp_ignored(port):
            if not ovn_utils.is_lsp_ignored(original_port):
                # From not ignored port to ignored port
                msg = (_('Updating device_owner to %(device_owner)s for port '
                         '%(port_id)s is not supported') %
                       {'device_owner': port['device_owner'],
                        'port_id': port['id']})
                raise OVNPortUpdateError(resource='port', msg=msg)
        elif ovn_utils.is_lsp_ignored(original_port):
            # From ignored port to not ignored port
            msg = (_('Updating device_owner for port %(port_id)s owned by '
                     '%(device_owner)s is not supported') %
                   {'port_id': port['id'],
                    'device_owner': original_port['device_owner']})
            raise OVNPortUpdateError(resource='port', msg=msg)

    def create_port_postcommit(self, context):
        """Create a port.

        :param context: PortContext instance describing the port.

        Called after the transaction completes. Call can block, though
        will block the entire process so care should be taken to not
        drastically affect performance.  Raising an exception will
        result in the deletion of the resource.
        """
        port = copy.deepcopy(context.current)
        port['network'] = context.network.current
        self._ovn_client.create_port(context._plugin_context, port)
        self._notify_dhcp_updated(port['id'])

    def update_port_precommit(self, context):
        """Update resources of a port.

        :param context: PortContext instance describing the new
        state of the port, as well as the original state prior
        to the update_port call.

        Called inside transaction context on session to complete a
        port update as defined by this mechanism driver. Raising an
        exception will result in rollback of the transaction.

        update_port_precommit is called for all changes to the port
        state. It is up to the mechanism driver to ignore state or
        state changes that it does not know or care about.
        """
        port = context.current
        original_port = context.original
        self._validate_ignored_port(port, original_port)
        ovn_utils.validate_and_get_data_from_binding_profile(port)
        self._validate_port_extra_dhcp_opts(port)
        if self._is_port_provisioning_required(port, context.host,
                                               context.original_host):
            self._insert_port_provisioning_block(context._plugin_context,
                                                 port['id'])

        if ovn_utils.is_lsp_router_port(port):
            # handle the case when an existing port is added to a
            # logical router so we need to track the creation of the lrp
            if not ovn_utils.is_lsp_router_port(original_port):
                ovn_revision_numbers_db.create_initial_revision(
                    context._plugin_context, port['id'],
                    ovn_const.TYPE_ROUTER_PORTS, may_exist=True,
                    std_attr_id=context.current['standard_attr_id'])

    def update_port_postcommit(self, context):
        """Update a port.

        :param context: PortContext instance describing the new
        state of the port, as well as the original state prior
        to the update_port call.

        Called after the transaction completes. Call can block, though
        will block the entire process so care should be taken to not
        drastically affect performance.  Raising an exception will
        result in the deletion of the resource.

        update_port_postcommit is called for all changes to the port
        state. It is up to the mechanism driver to ignore state or
        state changes that it does not know or care about.
        """
        port = copy.deepcopy(context.current)
        port['network'] = context.network.current
        original_port = copy.deepcopy(context.original)
        original_port['network'] = context.network.current

        # NOTE(mjozefcz): Check if port is in migration state. If so update
        # the port status from DOWN to UP in order to generate 'fake'
        # vif-interface-plugged event. This workaround is needed to
        # perform live-migration with live_migration_wait_for_vif_plug=True.
        if ((port['status'] == const.PORT_STATUS_DOWN and
             ovn_const.MIGRATING_ATTR in port[portbindings.PROFILE].keys() and
             port[portbindings.VIF_TYPE] in (
                 portbindings.VIF_TYPE_OVS,
                 portbindings.VIF_TYPE_VHOST_USER))):
            LOG.info("Setting port %s status from DOWN to UP in order "
                     "to emit vif-interface-plugged event.",
                     port['id'])
            self._plugin.update_port_status(context._plugin_context,
                                            port['id'],
                                            const.PORT_STATUS_ACTIVE)
            # The revision has been changed. In the meantime
            # port-update event already updated the OVN configuration,
            # So there is no need to update it again here. Anyway it
            # will fail that OVN has port with bigger revision.
            return

        self._ovn_client.update_port(context._plugin_context, port,
                                     port_object=original_port)
        self._notify_dhcp_updated(port['id'])

    def delete_port_postcommit(self, context):
        """Delete a port.

        :param context: PortContext instance describing the current
        state of the port, prior to the call to delete it.

        Called after the transaction completes. Call can block, though
        will block the entire process so care should be taken to not
        drastically affect performance.  Runtime errors are not
        expected, and will not prevent the resource from being
        deleted.
        """
        port = copy.deepcopy(context.current)
        port['network'] = context.network.current
        # FIXME(lucasagomes): PortContext does not have a session, therefore
        # we need to use the _plugin_context attribute.
        self._ovn_client.delete_port(context._plugin_context, port['id'],
                                     port_object=port)

    def bind_port(self, context):
        """Attempt to bind a port.

        :param context: PortContext instance describing the port

        This method is called outside any transaction to attempt to
        establish a port binding using this mechanism driver. Bindings
        may be created at each of multiple levels of a hierarchical
        network, and are established from the top level downward. At
        each level, the mechanism driver determines whether it can
        bind to any of the network segments in the
        context.segments_to_bind property, based on the value of the
        context.host property, any relevant port or network
        attributes, and its own knowledge of the network topology. At
        the top level, context.segments_to_bind contains the static
        segments of the port's network. At each lower level of
        binding, it contains static or dynamic segments supplied by
        the driver that bound at the level above. If the driver is
        able to complete the binding of the port to any segment in
        context.segments_to_bind, it must call context.set_binding
        with the binding details. If it can partially bind the port,
        it must call context.continue_binding with the network
        segments to be used to bind at the next lower level.

        If the binding results are committed after bind_port returns,
        they will be seen by all mechanism drivers as
        update_port_precommit and update_port_postcommit calls. But if
        some other thread or process concurrently binds or updates the
        port, these binding results will not be committed, and
        update_port_precommit and update_port_postcommit will not be
        called on the mechanism drivers with these results. Because
        binding results can be discarded rather than committed,
        drivers should avoid making persistent state changes in
        bind_port, or else must ensure that such state changes are
        eventually cleaned up.

        Implementing this method explicitly declares the mechanism
        driver as having the intention to bind ports. This is inspected
        by the QoS service to identify the available QoS rules you
        can use with ports.
        """
        port = context.current
        vnic_type = port.get(portbindings.VNIC_TYPE, portbindings.VNIC_NORMAL)
        if vnic_type not in self.supported_vnic_types:
            LOG.debug('Refusing to bind port %(port_id)s due to unsupported '
                      'vnic_type: %(vnic_type)s',
                      {'port_id': port['id'], 'vnic_type': vnic_type})
            return

        if ovn_utils.is_port_external(port):
            LOG.debug("Refusing to bind port due to unsupported vnic_type: %s "
                      "with no switchdev capability", vnic_type)
            return

        # OVN chassis information is needed to ensure a valid port bind.
        # Collect port binding data and refuse binding if the OVN chassis
        # cannot be found.
        chassis_physnets = []
        try:
            datapath_type, iface_types, chassis_physnets = (
                self.sb_ovn.get_chassis_data_for_ml2_bind_port(context.host))
            iface_types = iface_types.split(',') if iface_types else []
        except RuntimeError:
            LOG.debug('Refusing to bind port %(port_id)s due to '
                      'no OVN chassis for host: %(host)s',
                      {'port_id': port['id'], 'host': context.host})
            return

        for segment_to_bind in context.segments_to_bind:
            network_type = segment_to_bind['network_type']
            segmentation_id = segment_to_bind['segmentation_id']
            physical_network = segment_to_bind['physical_network']
            LOG.debug('Attempting to bind port %(port_id)s on host %(host)s '
                      'for network segment with type %(network_type)s, '
                      'segmentation ID %(segmentation_id)s, '
                      'physical network %(physical_network)s',
                      {'port_id': port['id'],
                       'host': context.host,
                       'network_type': network_type,
                       'segmentation_id': segmentation_id,
                       'physical_network': physical_network})
            # TODO(rtheis): This scenario is only valid on an upgrade from
            # neutron ML2 OVS since invalid network types are prevented during
            # network creation and update. The upgrade should convert invalid
            # network types. Once bug/1621879 is fixed, refuse to bind
            # ports with unsupported network types.
            if not self._is_network_type_supported(network_type):
                LOG.info('Upgrade allowing bind port %(port_id)s with '
                         'unsupported network type: %(network_type)s',
                         {'port_id': port['id'],
                          'network_type': network_type})

            if ((network_type in ['flat', 'vlan']) and
                    (physical_network not in chassis_physnets)):
                LOG.info('Refusing to bind port %(port_id)s on '
                         'host %(host)s due to the OVN chassis '
                         'bridge mapping physical networks '
                         '%(chassis_physnets)s not supporting '
                         'physical network: %(physical_network)s',
                         {'port_id': port['id'],
                          'host': context.host,
                          'chassis_physnets': chassis_physnets,
                          'physical_network': physical_network})
            else:
                if (datapath_type == ovn_const.CHASSIS_DATAPATH_NETDEV and
                        ovn_const.CHASSIS_IFACE_DPDKVHOSTUSER in iface_types):
                    vhost_user_socket = ovn_utils.ovn_vhu_sockpath(
                        ovn_conf.get_ovn_vhost_sock_dir(), port['id'])
                    vif_type = portbindings.VIF_TYPE_VHOST_USER
                    port[portbindings.VIF_DETAILS].update({
                        portbindings.VHOST_USER_SOCKET: vhost_user_socket})
                    vif_details = dict(self.vif_details[vif_type])
                    vif_details[portbindings.VHOST_USER_SOCKET] = (
                        vhost_user_socket)
                else:
                    vif_type = portbindings.VIF_TYPE_OVS
                    vif_details = self.vif_details[vif_type]

                context.set_binding(segment_to_bind[api.ID], vif_type,
                                    vif_details)
                break

    def get_workers(self):
        """Get any worker instances that should have their own process

        Any driver that needs to run processes separate from the API or RPC
        workers, can return a sequence of worker instances.
        """
        # See doc/source/design/ovn_worker.rst for more details.
        return [worker.MaintenanceWorker()]

    def _update_dnat_entry_if_needed(self, port_id, up=True):
        """Update DNAT entry if using distributed floating ips."""
        if not self.nb_ovn:
            self.nb_ovn = self._ovn_client._nb_idl

        nat = self.nb_ovn.db_find('NAT',
                                  ('logical_port', '=', port_id),
                                  ('type', '=', 'dnat_and_snat')).execute()
        if not nat:
            return
        # We take first entry as one port can only have one FIP
        nat = nat[0]
        # If the external_id doesn't exist, let's create at this point.
        # TODO(dalvarez): Remove this code in T cycle when we're sure that
        # all DNAT entries have the external_id.
        if not nat['external_ids'].get(ovn_const.OVN_FIP_EXT_MAC_KEY):
            self.nb_ovn.db_set('NAT', nat['_uuid'],
                               ('external_ids',
                               {ovn_const.OVN_FIP_EXT_MAC_KEY:
                                nat['external_mac']})).execute()

        if up and ovn_conf.is_ovn_distributed_floating_ip():
            mac = nat['external_ids'][ovn_const.OVN_FIP_EXT_MAC_KEY]
            if nat['external_mac'] != mac:
                LOG.debug("Setting external_mac of port %s to %s",
                          port_id, mac)
                self.nb_ovn.db_set(
                    'NAT', nat['_uuid'], ('external_mac', mac)).execute(
                    check_error=True)
        else:
            if nat['external_mac']:
                LOG.debug("Clearing up external_mac of port %s", port_id)
                self.nb_ovn.db_clear(
                    'NAT', nat['_uuid'], 'external_mac').execute(
                    check_error=True)

    def _should_notify_nova(self, db_port):
        # NOTE(twilson) It is possible for a test to override a config option
        # after the plugin has been initialized so the nova_notifier attribute
        # is not set on the plugin
        return (cfg.CONF.notify_nova_on_port_status_changes and
                hasattr(self._plugin, 'nova_notifier') and
                db_port.device_owner.startswith(
                    const.DEVICE_OWNER_COMPUTE_PREFIX))

    def set_port_status_up(self, port_id):
        # Port provisioning is complete now that OVN has reported that the
        # port is up. Any provisioning block (possibly added during port
        # creation or when OVN reports that the port is down) must be removed.
        LOG.info("OVN reports status up for port: %s", port_id)

        self._update_dnat_entry_if_needed(port_id)

        admin_context = n_context.get_admin_context()
        provisioning_blocks.provisioning_complete(
            admin_context,
            port_id,
            resources.PORT,
            provisioning_blocks.L2_AGENT_ENTITY)

        try:
            # NOTE(lucasagomes): Router ports in OVN is never bound
            # to a host given their decentralized nature. By calling
            # provisioning_complete() - as above - don't do it for us
            # becasue the router ports are unbind so, for OVN we are
            # forcing the status here. Maybe it's something that we can
            # change in core Neutron in the future.
            db_port = ml2_db.get_port(admin_context, port_id)
            if not db_port:
                return

            if db_port.device_owner in (const.DEVICE_OWNER_ROUTER_INTF,
                                        const.DEVICE_OWNER_DVR_INTERFACE,
                                        const.DEVICE_OWNER_ROUTER_HA_INTF):
                self._plugin.update_port_status(admin_context, port_id,
                                                const.PORT_STATUS_ACTIVE)
            elif self._should_notify_nova(db_port):
                self._plugin.nova_notifier.notify_port_active_direct(db_port)
        except (os_db_exc.DBReferenceError, n_exc.PortNotFound):
            LOG.debug('Port not found during OVN status up report: %s',
                      port_id)

    def set_port_status_down(self, port_id):
        # Port provisioning is required now that OVN has reported that the
        # port is down. Insert a provisioning block and mark the port down
        # in neutron. The block is inserted before the port status update
        # to prevent another entity from bypassing the block with its own
        # port status update.
        LOG.info("OVN reports status down for port: %s", port_id)
        self._update_dnat_entry_if_needed(port_id, False)
        admin_context = n_context.get_admin_context()
        try:
            db_port = ml2_db.get_port(admin_context, port_id)
            if not db_port:
                return

            self._insert_port_provisioning_block(admin_context, port_id)
            self._plugin.update_port_status(admin_context, port_id,
                                            const.PORT_STATUS_DOWN)

            if self._should_notify_nova(db_port):
                self._plugin.nova_notifier.record_port_status_changed(
                    db_port, const.PORT_STATUS_ACTIVE, const.PORT_STATUS_DOWN,
                    None)
                self._plugin.nova_notifier.send_port_status(
                    None, None, db_port)
        except (os_db_exc.DBReferenceError, n_exc.PortNotFound):
            LOG.debug("Port not found during OVN status down report: %s",
                      port_id)

    def delete_mac_binding_entries(self, external_ip):
        """Delete all MAC_Binding entries associated to this IP address"""
        cmd = ['ovsdb-client', 'transact', ovn_conf.get_ovn_sb_connection(),
               '--timeout', str(ovn_conf.get_ovn_ovsdb_timeout())]

        if ovn_conf.get_ovn_sb_private_key():
            cmd += ['-p', ovn_conf.get_ovn_sb_private_key(), '-c',
                    ovn_conf.get_ovn_sb_certificate(), '-C',
                    ovn_conf.get_ovn_sb_ca_cert()]

        cmd += ['["OVN_Southbound", {"op": "delete", "table": "MAC_Binding", '
                '"where": [["ip", "==", "%s"]]}]' % external_ip]

        return processutils.execute(*cmd,
                                    log_errors=processutils.LOG_FINAL_ERROR)

    def update_segment_host_mapping(self, host, phy_nets):
        """Update SegmentHostMapping in DB"""
        if not host:
            return

        ctx = n_context.get_admin_context()
        segments = segment_service_db.get_segments_with_phys_nets(
            ctx, phy_nets)

        available_seg_ids = {
            segment['id'] for segment in segments
            if segment['network_type'] in ('flat', 'vlan')}

        segment_service_db.update_segment_host_mapping(
            ctx, host, available_seg_ids)

    def _add_segment_host_mapping_for_segment(self, resource, event, trigger,
                                              payload=None):
        context = payload.context
        segment = payload.latest_state
        phynet = segment.physical_network
        if not phynet:
            return

        host_phynets_map = self.sb_ovn.get_chassis_hostname_and_physnets()
        hosts = {host for host, phynets in host_phynets_map.items()
                 if phynet in phynets}
        segment_service_db.map_segment_to_hosts(context, segment.id, hosts)

    def patch_plugin_merge(self, method_name, new_fn, op=operator.add):
        old_method = getattr(self._plugin, method_name)

        @functools.wraps(old_method)
        def fn(slf, *args, **kwargs):
            new_method = types.MethodType(new_fn, self._plugin)
            results = old_method(*args, **kwargs)
            return op(results, new_method(*args, _driver=self, **kwargs))

        setattr(self._plugin, method_name, types.MethodType(fn, self._plugin))

    def patch_plugin_choose(self, method_name, new_fn):
        old_method = getattr(self._plugin, method_name)

        @functools.wraps(old_method)
        def fn(slf, *args, **kwargs):
            new_method = types.MethodType(new_fn, self._plugin)
            try:
                return new_method(*args, _driver=self, **kwargs)
            except n_exc.NotFound:
                return old_method(*args, **kwargs)

        setattr(self._plugin, method_name, types.MethodType(fn, self._plugin))

    def ping_all_chassis(self):
        """Update NB_Global.nb_cfg so that Chassis.nb_cfg will increment

        :returns: (bool) True if nb_cfg was updated. False if it was updated
            recently and this call didn't trigger any update.
        """
        last_ping = self.nb_ovn.nb_global.external_ids.get(
            ovn_const.OVN_LIVENESS_CHECK_EXT_ID_KEY)
        if last_ping:
            interval = max(cfg.CONF.agent_down_time // 2, 1)
            next_ping = (timeutils.parse_isotime(last_ping) +
                         datetime.timedelta(seconds=interval))
            if timeutils.utcnow(with_timezone=True) < next_ping:
                return False

        with self.nb_ovn.create_transaction(check_error=True,
                                            bump_nb_cfg=True) as txn:
            txn.add(self.nb_ovn.check_liveness())
        return True

    def list_availability_zones(self, context, filters=None):
        """List all availability zones from gateway chassis."""
        azs = {}
        # TODO(lucasagomes): In the future, once the agents API in OVN
        # gets more stable we should consider getting the information from
        # the availability zones from the agents API itself. That would
        # allow us to do things like: Do not schedule router ports on
        # chassis that are offline (via the "alive" attribute for agents).
        for ch in self.sb_ovn.chassis_list().execute(check_error=True):
            # Only take in consideration gateway chassis because that's where
            # the router ports are scheduled on
            if not ovn_utils.is_gateway_chassis(ch):
                continue

            azones = ovn_utils.get_chassis_availability_zones(ch)
            for azone in azones:
                azs[azone] = {'name': azone, 'resource': 'router',
                              'state': 'available',
                              'tenant_id': context.project_id}
        return azs


def get_agents(self, context, filters=None, fields=None, _driver=None):
    _driver.ping_all_chassis()
    filters = filters or {}
    agent_list = []
    for agent in n_agent.AgentCache():
        agent_dict = agent.as_dict()
        if all(agent_dict[k] in v for k, v in filters.items()):
            agent_list.append(agent_dict)
    return agent_list


def get_agent(self, context, id, fields=None, _driver=None):
    try:
        return n_agent.AgentCache()[id].as_dict()
    except KeyError:
        raise n_exc.agent.AgentNotFound(id=id)


def update_agent(self, context, id, agent, _driver=None):
    ovn_agent = get_agent(self, None, id, _driver=_driver)
    chassis_name = ovn_agent['configurations']['chassis_name']
    agent_type = ovn_agent['agent_type']
    agent = agent['agent']
    # neutron-client always passes admin_state_up, openstack client doesn't
    # and we can just fall through to raising in the case that admin_state_up
    # is being set to False, otherwise the end-state will be fine
    if not agent.get('admin_state_up', True):
        pass
    elif 'description' in agent:
        _driver.sb_ovn.set_chassis_neutron_description(
            chassis_name, agent['description'],
            agent_type).execute(check_error=True)
        return agent
    else:
        # admin_state_up=True w/o description
        return agent
    raise n_exc.BadRequest(resource='agent',
                           msg='OVN agent status cannot be updated')


def delete_agent(self, context, id, _driver=None):
    # raise AgentNotFound if this isn't an ml2/ovn-related agent
    agent = get_agent(self, None, id, _driver=_driver)

    # NOTE(twilson) According to the API docs, an agent must be disabled
    # before deletion. Otherwise, behavior seems to be undefined. We could
    # check that alive=False before allowing deletion, but depending on the
    # agent_down_time setting, that could take quite a while.
    # If ovn-controller is up, the Chassis will be recreated and so the agent
    # will still show as up. The recreated Chassis will cause all kinds of
    # events to fire. But again, undefined behavior.
    chassis_name = agent['configurations']['chassis_name']
    _driver.sb_ovn.chassis_del(chassis_name, if_exists=True).execute(
        check_error=True)
    # Send a specific event that all API workers can get to delete the agent
    # from their caches. Ideally we could send a single transaction that both
    # created and deleted the key, but alas python-ovs is too "smart"
    _driver.sb_ovn.db_set(
        'SB_Global', '.', ('external_ids', {'delete_agent': str(id)})).execute(
            check_error=True)
    _driver.sb_ovn.db_remove(
        'SB_Global', '.', 'external_ids', delete_agent=str(id),
        if_exists=True).execute(check_error=True)


def create_default_drop_port_group(nb_idl):
    pg_name = ovn_const.OVN_DROP_PORT_GROUP_NAME
    if nb_idl.get_port_group(pg_name):
        LOG.debug("Port Group %s already exists", pg_name)
        return
    with nb_idl.transaction(check_error=True) as txn:
        # If drop Port Group doesn't exist yet, create it.
        txn.add(nb_idl.pg_add(pg_name, acls=[], may_exist=True))
        # Add ACLs to this Port Group so that all traffic is dropped.
        acls = ovn_acl.add_acls_for_drop_port_group(pg_name)
        for acl in acls:
            txn.add(nb_idl.pg_acl_add(may_exist=True, **acl))

        ports_with_pg = set()
        for pg in nb_idl.get_sg_port_groups().values():
            ports_with_pg.update(pg['ports'])

        if ports_with_pg:
            # Add the ports to the default Port Group
            txn.add(nb_idl.pg_add_ports(pg_name, list(ports_with_pg)))


def get_availability_zones(cls, context, _driver, filters=None, fields=None,
                           sorts=None, limit=None, marker=None,
                           page_reverse=False):
    return list(_driver.list_availability_zones(context, filters).values())


def validate_availability_zones(cls, context, resource_type,
                                availability_zones, _driver):
    if not availability_zones or resource_type != 'network':
        return

    azs = {az['name'] for az in
           _driver.list_availability_zones(context).values()}
    diff = set(availability_zones) - azs
    if diff:
        raise az_exc.AvailabilityZoneNotFound(
            availability_zone=', '.join(diff))
