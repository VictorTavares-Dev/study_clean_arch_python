from src.adapters.db_nosql_manager import NoSQLDBManager


class ManageNoSQLDatabase:
    def __init__(self, dynamodb_manager: NoSQLDBManager):
        """
        Inicializa o caso de uso de gerenciamento de banco NoSQL, com o
        adaptador DynamoDBManager.
        :param dynamodb_manager: Classe adaptadora para o DynamoDB.
        """
        self.dynamodb_manager = dynamodb_manager

    def save_item(self, item_data: dict):
        """
        Salva um item no DynamoDB.
        :param item_data: Dicionário com os dados do item a ser salvo.
        """
        self.dynamodb_manager.save_item(item_data)

    def get_item(self, item_id: str):
        """
        Recupera um item do DynamoDB.
        :param item_id: ID do item a ser recuperado.
        :return: Dados do item ou None se não encontrado.
        """
        return self.dynamodb_manager.get_item(item_id)
