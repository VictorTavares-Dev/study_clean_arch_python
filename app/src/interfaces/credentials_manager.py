from abc import ABC, abstractmethod


class ICredentialsManager(ABC):
    @abstractmethod
    def assume_role(self, role_arn: str, session_name: str) -> tuple:
        """
        Assume uma role no AWS STS e retorna as credenciais temporárias.
        :param role_arn: ARN da role a ser assumida.
        :param session_name: Nome da sessão.
        :return: Tupla com as credenciais temporárias.
        """
        pass
