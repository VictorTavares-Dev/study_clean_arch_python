from abc import ABC, abstractmethod


class IRAMService(ABC):
    """
    AWS Resource Access Manager interface.
    """

    @abstractmethod
    def get_resource_shares(self, resource_owner: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    def list_resource_share_permissions(self, resource_share_arn: str) -> dict:
        raise NotImplementedError
