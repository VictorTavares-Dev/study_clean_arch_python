class NoSQLItem:
    def __init__(self, item_id: str, data: dict):
        self.item_id = item_id
        self.data = data

    def to_dict(self):
        """Converte o item para um formato de dicionário."""
        return {"item_id": self.item_id, "data": self.data}

    @classmethod
    def from_dict(cls, data):
        """Cria uma instância de NoSQLItem a partir de um dicionário."""
        return cls(data["item_id"], data["data"])
