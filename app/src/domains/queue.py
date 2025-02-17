class QueueMessage:
    def __init__(self, message_body: str, message_id: str, sent_at: str):
        self.message_body = message_body
        self.message_id = message_id
        self.sent_at = sent_at

    def to_dict(self):
        """Converte a mensagem para um formato de dicionário."""
        return {
            "message_body": self.message_body,
            "message_id": self.message_id,
            "sent_at": self.sent_at,
        }

    @classmethod
    def from_dict(cls, data):
        """Cria uma instância de SQSMessage a partir de um dicionário."""
        return cls(data["message_body"], data["message_id"], data["sent_at"])
