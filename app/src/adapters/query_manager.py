import boto3


class QueryManager:
    def __init__(self):
        self.athena_client = boto3.client("athena")

    def execute_query(self, query: str, database: str, output_location: str):
        response = self.athena_client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={"Database": database},
            ResultConfiguration={"OutputLocation": output_location},
        )
        return response["QueryExecutionId"]

    def get_query_results(self, query_execution_id: str):
        result = self.athena_client.get_query_results(
            QueryExecutionId=query_execution_id
        )
        return result["ResultSet"]["Rows"]
