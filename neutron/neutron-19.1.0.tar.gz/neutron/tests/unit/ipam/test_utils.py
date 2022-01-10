# Copyright (c) 2015 Mirantis, Inc.
# All Rights Reserved.
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

import netaddr
from neutron_lib import constants

from neutron.ipam import utils
from neutron.tests import base


class TestIpamUtils(base.BaseTestCase):

    def test_check_subnet_ip_v4_network(self):
        self.assertFalse(utils.check_subnet_ip('1.1.1.0/24', '1.1.1.0'))

    def test_check_subnet_ip_v4_broadcast(self):
        self.assertFalse(utils.check_subnet_ip('1.1.1.0/24', '1.1.1.255'))

    def test_check_subnet_ip_v4_valid(self):
        self.assertTrue(utils.check_subnet_ip('1.1.1.0/24', '1.1.1.1'))
        self.assertTrue(utils.check_subnet_ip('1.1.1.0/24', '1.1.1.254'))

    def test_check_subnet_ip_v6_owner_router_or_not_defined(self):
        for port_owner in (constants.ROUTER_PORT_OWNERS + ('', )):
            # IP address == network
            self.assertTrue(utils.check_subnet_ip('F111::0/64', 'F111::0',
                                                  port_owner=port_owner))
            # IP address == broadcast
            self.assertTrue(utils.check_subnet_ip(
                'F111::0/64', 'F111::FFFF:FFFF:FFFF:FFFF',
                port_owner=port_owner))
            # IP address in network
            self.assertTrue(utils.check_subnet_ip('F111::0/64', 'F111::50',
                                                  port_owner=port_owner))
            # IP address not in network
            self.assertFalse(utils.check_subnet_ip('F111::0/64', 'F112::50',
                                                   port_owner=port_owner))

    def test_check_subnet_ip_v6_owner_not_router(self):
        port_owner = 'nova:compute'
        # IP address == network
        self.assertFalse(utils.check_subnet_ip('F111::0/64', 'F111::0',
                                               port_owner=port_owner))
        # IP address == broadcast
        self.assertTrue(utils.check_subnet_ip(
            'F111::0/64', 'F111::FFFF:FFFF:FFFF:FFFF',
            port_owner=port_owner))
        # IP address in network
        self.assertTrue(utils.check_subnet_ip('F111::0/64', 'F111::50',
                                              port_owner=port_owner))
        # IP address not in network
        self.assertFalse(utils.check_subnet_ip('F111::0/64', 'F112::50',
                                               port_owner=port_owner))

    def test_generate_pools_v4_nogateway(self):
        cidr = '192.168.0.0/24'
        expected = [netaddr.IPRange('192.168.0.1', '192.168.0.254')]
        self.assertEqual(expected, utils.generate_pools(cidr, None))

    def test_generate_pools_v4_gateway_first(self):
        cidr = '192.168.0.0/24'
        gateway = '192.168.0.1'
        expected = [netaddr.IPRange('192.168.0.2', '192.168.0.254')]
        self.assertEqual(expected, utils.generate_pools(cidr, gateway))

    def test_generate_pools_v4_gateway_last(self):
        cidr = '192.168.0.0/24'
        gateway = '192.168.0.254'
        expected = [netaddr.IPRange('192.168.0.1', '192.168.0.253')]
        self.assertEqual(expected, utils.generate_pools(cidr, gateway))

    def test_generate_pools_v4_32(self):
        # 32 is special because it should have 1 usable address
        cidr = '192.168.0.0/32'
        expected = [netaddr.IPRange('192.168.0.0', '192.168.0.0')]
        self.assertEqual(expected, utils.generate_pools(cidr, None))

    def test_generate_pools_v4_31(self):
        cidr = '192.168.0.0/31'
        expected = [netaddr.IPRange('192.168.0.0', '192.168.0.1')]
        self.assertEqual(expected, utils.generate_pools(cidr, None))

    def test_generate_pools_v4_gateway_middle(self):
        cidr = '192.168.0.0/24'
        gateway = '192.168.0.128'
        expected = [netaddr.IPRange('192.168.0.1', '192.168.0.127'),
                    netaddr.IPRange('192.168.0.129', '192.168.0.254')]
        self.assertEqual(expected, utils.generate_pools(cidr, gateway))

    def test_generate_pools_v6_nogateway(self):
        # other than the difference in the last address, the rest of the
        # logic is the same as v4 so we only need one test
        cidr = 'F111::0/64'
        expected = [netaddr.IPRange('F111::1', 'F111::FFFF:FFFF:FFFF:FFFF')]
        self.assertEqual(expected, utils.generate_pools(cidr, None))

    def test_generate_pools_v6_empty(self):
        # We want to be sure the range will begin and end with an IPv6
        # address, even if an ambiguous ::/64 cidr is given.
        cidr = '::/64'
        expected = [netaddr.IPRange('::1', '::FFFF:FFFF:FFFF:FFFF')]
        self.assertEqual(expected, utils.generate_pools(cidr, None))

    def test_check_gateway_invalid_in_subnet(self):
        data = [('10.0.0.1', '10.0.0.0/8', False),
                ('10.255.255.255', '10.0.0.0/8', True),
                ('10.0.0.0', '10.0.0.0/8', True),
                ('192.168.100.10', '10.0.0.0/8', False),
                ('2001:db8::1', '2001:db8::/64', False),
                ]
        for gw_ip, network_cidr, result in data:
            self.assertEqual(result, utils.check_gateway_invalid_in_subnet(
                network_cidr, gw_ip))
