import boto3
import logging
from typing import Optional
from src.adapter.utils import retry_with_backoff
from src.use_case.interfaces.ram_service_interface import IRAMService


class RAMAdapter(IRAMService):
    retriable_errors = [
        "ServerInternalException",
        "ServiceUnavailableException",
    ]

    def __init__(
        self,
        credentials: Optional[dict] = None,
        region_name: Optional[str] = "sa-east-1",
    ):
        self.logger = logging.getLogger(__name__)
        self.region_name = (
            region_name if region_name else boto3.Session().region_name
        )
        if credentials:
            self.logger.info(
                "Credentials provided, creating RAM client with them."
            )
            self.credentials = credentials
            self.__ram_client = boto3.client(
                "ram",
                region_name=self.region_name,
                aws_access_key_id=self.credentials["AccessKeyId"],
                aws_secret_access_key=self.credentials["SecretAccessKey"],
                aws_session_token=self.credentials["SessionToken"],
            )
        else:
            self.logger.info(
                "No credentials provided, using default credentials."
            )
            self.__ram_client = boto3.client(
                "ram", region_name=self.region_name
            )

    def get_resource_shares(self, resource_owner: str) -> dict:
        """
        Retrieve resource shares for a specified resource owner.

        Logs the invocation and calls the underlying RAM client to fetch
        resource shares, applying a retry mechanism for retriable errors.

        Args:
            resource_owner (str): The identifier of the resource owner whose
                resource shares are to be retrieved. Possible values are
                "SELF" for the current account or "OTHER-ACCOUNTS" for
                external accounts.

        Returns:
            dict: A dictionary containing the resource shares associated with
                the specified resource owner.

        Raises:
            Exception: Propagates exceptions that are not considered retriable
                by the retry mechanism.
        """
        self.logger.info(
            "Calling get_resource_shares with "
            f"resourceOwner={resource_owner!r}"
        )
        return retry_with_backoff(
            func=self.__ram_client.get_resource_shares,
            params={"resourceOwner": resource_owner},
            errors=RAMAdapter.retriable_errors,
        )

    def list_resource_share_permissions(self, resource_share_arn: str) -> dict:
        """
        Retrieves the permissions associated with a specified AWS Resource
        Access Manager (RAM) resource share.

        Args:
            resource_share_arn (str): The Amazon Resource Name (ARN) of the
                resource share whose permissions are to be listed.

        Returns:
            dict: A dictionary containing the permissions for the specified
                resource share.

        Raises:
            Exception: Propagates exceptions raised by the underlying RAM
                client, except for retriable errors which are handled with
                backoff.
        """
        self.logger.info(
            "Calling list_resource_share_permissions with "
            f"resourceShareArn={resource_share_arn!r}"
        )
        return retry_with_backoff(
            func=self.__ram_client.list_resource_share_permissions,
            params={"resourceShareArn": resource_share_arn},
            errors=RAMAdapter.retriable_errors,
        )
