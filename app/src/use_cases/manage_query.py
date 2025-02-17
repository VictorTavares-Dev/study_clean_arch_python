from src.adapters.query_manager import QueryManager


class ManageQuery:
    def __init__(self, query_manager: QueryManager):
        """
        Inicializa o caso de uso para gerenciar consultas no Athena, com o
        adaptador QueryManager.
        :param query_manager: Classe adaptadora para o Athena.
        """
        self.query_manager = query_manager()

    def run_query(self, query_string: str):
        """
        Executa uma consulta no Athena e retorna os resultados.
        :param query_string: A string de consulta a ser executada.
        :return: Resultados da consulta.
        """
        query_execution_id = self.query_manager.run_query(query_string)
        results = self.query_manager.get_query_results(query_execution_id)
        return results
