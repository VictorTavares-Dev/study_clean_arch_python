import boto3
from botocore.exceptions import ClientError
from src.interfaces.db_nosql_manager import INoSQLDBManager


class NoSQLDBManager(INoSQLDBManager):
    def __init__(self, table_name: str):
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(table_name)

    def save_item(self, item: dict):
        try:
            self.table.put_item(Item=item)
        except ClientError as e:
            print(f"Erro ao salvar item: {e.response['Error']['Message']}")

    def get_item(self, key: dict):
        try:
            response = self.table.get_item(Key=key)
            return response.get("Item", None)
        except ClientError as e:
            print(f"Erro ao obter item: {e.response['Error']['Message']}")
