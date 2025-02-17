import boto3


class FilesManager:
    def __init__(self):
        self.s3_client = boto3.client("s3")

    def upload_file(self, bucket_name: str, file_name: str, file_data: bytes):
        try:
            self.s3_client.put_object(
                Bucket=bucket_name, Key=file_name, Body=file_data
            )
        except Exception as e:
            print(f"Erro ao fazer upload do arquivo: {e}")

    def download_file(self, bucket_name: str, file_name: str) -> bytes:
        try:
            response = self.s3_client.get_object(
                Bucket=bucket_name, Key=file_name
            )
            return response["Body"].read()
        except Exception as e:
            print(f"Erro ao baixar o arquivo: {e}")
