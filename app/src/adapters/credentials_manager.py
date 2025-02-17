from interfaces.credentials_manager import ICredentialsManager
import boto3


class CredentialsManager(ICredentialsManager):
    def __init__(self):
        self.sts_client = boto3.client("sts")

    def assume_role(self, role_arn: str, session_name: str):
        response = self.sts_client.assume_role(
            RoleArn=role_arn, RoleSessionName=session_name
        )
        credentials = response["Credentials"]
        return (
            credentials["AccessKeyId"],
            credentials["SecretAccessKey"],
            credentials["SessionToken"],
        )
