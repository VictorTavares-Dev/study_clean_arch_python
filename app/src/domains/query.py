class Query:
    def __init__(
        self, query_execution_id: str, query_string: str, results: list
    ):
        self.query_execution_id = query_execution_id
        self.query_string = query_string
        self.results = results

    def to_dict(self):
        """Converte o resultado da consulta para um formato de dicionário."""
        return {
            "query_execution_id": self.query_execution_id,
            "query_string": self.query_string,
            "results": self.results,
        }

    @classmethod
    def from_dict(cls, data):
        """Cria uma instância de AthenaQueryResult a partir de um dicionário."""
        return cls(
            data["query_execution_id"], data["query_string"], data["results"]
        )
