from src.adapters.queue_manager import QueueManager


class ManageQueue:
    def __init__(self, queue_manager: QueueManager):
        """
        Inicializa o caso de uso de gerenciamento de filas, com o adaptador
        QueueManager.
        :param queue_manager: Classe adaptadora para o QueueManager.
        """
        self.queue_manager = queue_manager

    def send_message(self, message_body: str):
        """
        Envia uma mensagem para a fila.
        :param message_body: Corpo da mensagem a ser enviada para a fila.
        """
        self.queue_manager.send_message(message_body)
