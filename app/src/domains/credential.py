class Credential:
    def __init__(self, identifier: str, username: str, password: str):
        self.identifier = identifier
        self.username = username
        self.password = password

    def to_dict(self):
        """Converte a credencial para um formato de dicionário."""
        return {
            "identifier": self.identifier,
            "username": self.username,
            "password": self.password,
        }

    @classmethod
    def from_dict(cls, data):
        """Cria uma instância de Credential a partir de um dicionário."""
        return cls(data["identifier"], data["username"], data["password"])
