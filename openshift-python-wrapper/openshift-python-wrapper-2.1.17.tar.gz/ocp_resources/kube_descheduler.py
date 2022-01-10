from ocp_resources.constants import TIMEOUT_4MINUTES
from ocp_resources.resource import NamespacedResource


class KubeDescheduler(NamespacedResource):
    api_group = NamespacedResource.ApiGroup.OPERATOR_OPENSHIFT_IO

    def __init__(
        self,
        name=None,
        namespace=None,
        profiles=None,
        descheduling_interval=3600,
        log_level="Normal",
        managemet_state="Managed",
        operator_log_level="Normal",
        teardown=True,
        client=None,
        yaml_file=None,
        delete_timeout=TIMEOUT_4MINUTES,
    ):
        """
        Create Descheduler object.

        Args:
            profiles (list): list of descheduling profiles. Supported:
                - AffinityAndTaints
                - TopologyAndDuplicates
                - LifecycleAndUtilization
            log_level (str): logging of a component. Supported: "Normal", "Debug", "Trace", "TraceAll"
            operator_log_level (str): logging of an operator. Supported: "Normal", "Debug", "Trace", "TraceAll"
        """
        super().__init__(
            name=name,
            namespace=namespace,
            client=client,
            teardown=teardown,
            yaml_file=yaml_file,
            delete_timeout=delete_timeout,
        )
        self.profiles = profiles or ["AffinityAndTaints"]
        self.descheduling_interval = descheduling_interval
        self.log_level = log_level
        self.managemet_state = managemet_state
        self.operator_log_level = operator_log_level

    def to_dict(self):
        res = super().to_dict()
        if self.yaml_file:
            return res

        res.update(
            {
                "spec": {
                    "deschedulingIntervalSeconds": self.descheduling_interval,
                    "logLevel": self.log_level,
                    "managementState": self.managemet_state,
                    "operatorLogLevel": self.operator_log_level,
                    "profiles": self.profiles,
                }
            }
        )
        return res
