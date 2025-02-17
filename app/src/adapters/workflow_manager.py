import boto3


class WorkflowManager:
    def __init__(self):
        self.sfn_client = boto3.client("stepfunctions")

    def start_execution(self, state_machine_arn: str, input_data: dict):
        response = self.sfn_client.start_execution(
            stateMachineArn=state_machine_arn, input=str(input_data)
        )
        return response["executionArn"]

    def describe_execution(self, execution_arn: str):
        response = self.sfn_client.describe_execution(
            executionArn=execution_arn
        )
        return response
