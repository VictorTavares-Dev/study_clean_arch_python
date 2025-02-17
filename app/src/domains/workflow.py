class Workflow:
    def __init__(self, execution_arn: str, status: str, input_data: dict):
        self.execution_arn = execution_arn
        self.status = status
        self.input_data = input_data

    def to_dict(self):
        """Converte o fluxo de trabalho para um formato de dicionário."""
        return {
            "execution_arn": self.execution_arn,
            "status": self.status,
            "input_data": self.input_data,
        }

    @classmethod
    def from_dict(cls, data):
        """Cria uma instância de Workflow a partir de um dicionário."""
        return cls(data["execution_arn"], data["status"], data["input_data"])
