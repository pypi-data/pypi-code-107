from ocp_resources.constants import TIMEOUT_4MINUTES
from ocp_resources.mtv import MTV
from ocp_resources.resource import NamespacedResource


class Hook(NamespacedResource, MTV):
    """
    Migration Tool for Virtualization (MTV) Plan's Hook Resource.
    """

    api_group = NamespacedResource.ApiGroup.FORKLIFT_KONVEYOR_IO

    def __init__(
        self,
        name=None,
        namespace=None,
        image="quay.io/konveyor/hook-runner:latest",
        playbook=None,
        client=None,
        teardown=True,
        yaml_file=None,
        delete_timeout=TIMEOUT_4MINUTES,
    ):
        """
        Args:
            image (str): Path to an ansible image
            playbook (str): Ansible playbook to be performed
        """
        super().__init__(
            name=name,
            namespace=namespace,
            client=client,
            teardown=teardown,
            yaml_file=yaml_file,
            delete_timeout=delete_timeout,
        )
        self.image = image
        self.playbook = playbook

    def to_dict(self):
        res = super().to_dict()
        if self.yaml_file:
            return res

        res.update(
            {
                "spec": {
                    "image": self.image,
                    "playbook": self.playbook,
                },
            }
        )
        return res
