from src.adapters.credentials_manager import CredentialsManager


class ManageCredentials:
    def __init__(self, credentials_manager: CredentialsManager):
        """
        Inicializa o caso de uso de credenciais, com o adaptador
        CredentialsManager.
        - :param sts_credentials_manager: Classe adaptadora para o serviço de
        credenciais.
        """
        self.credentials_manager = credentials_manager

    def get_temporary_credentials(self, role_arn: str, session_name: str):
        """
        Obtém credenciais temporárias usando o STSCredentialsManager.
        :param role_arn: ARN da role a ser assumida.
        :param session_name: Nome da sessão de segurança.
        :return: Tupla contendo (access_key, secret_key, session_token).
        """
        credentials = self.credentials_manager.assume_role(
            role_arn, session_name
        )
        return (
            credentials["AccessKeyId"],
            credentials["SecretAccessKey"],
            credentials["SessionToken"],
        )
