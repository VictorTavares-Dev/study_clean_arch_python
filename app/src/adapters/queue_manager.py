import boto3


class QueueManager:
    def __init__(self, queue_url: str):
        self.sqs_client = boto3.client("sqs")
        self.queue_url = queue_url

    def send_message(self, message_body: str):
        self.sqs_client.send_message(
            QueueUrl=self.queue_url, MessageBody=message_body
        )

    def receive_message(self):
        response = self.sqs_client.receive_message(
            QueueUrl=self.queue_url, MaxNumberOfMessages=1
        )
        messages = response.get("Messages", [])
        return messages[0] if messages else None
