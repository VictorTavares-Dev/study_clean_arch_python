from abc import ABC, abstractmethod


class INoSQLDBManager(ABC):
    @abstractmethod
    def save_item(self, item: dict) -> None:
        """
        Salva um item na base de dados NoSQL.
        :param item: Item a ser salvo.
        :return: None
        """
        pass

    @abstractmethod
    def get_item(self, key: dict) -> dict:
        """
        Obtém um item da base de dados NoSQL.
        :param key: Chave do item a ser obtido.
        :return: Item obtido.
        """
        pass
