class File:
    def __init__(self, bucket_name: str, file_name: str, file_size: int):
        self.bucket_name = bucket_name
        self.file_name = file_name
        self.file_size = file_size

    def to_dict(self):
        """Converte o arquivo para um formato de dicionário."""
        return {
            "bucket_name": self.bucket_name,
            "file_name": self.file_name,
            "file_size": self.file_size,
        }

    @classmethod
    def from_dict(cls, data):
        """Cria uma instância de File a partir de um dicionário."""
        return cls(data["bucket_name"], data["file_name"], data["file_size"])
