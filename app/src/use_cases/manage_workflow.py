from src.adapters.workflow_manager import WorkflowManager


class ManageWorkflows:
    def __init__(self, workflow_manager: WorkflowManager):
        """
        Inicializa o caso de uso de gerenciamento de workflows no Step
        Functions, com o adaptador WorkflowManager.
        :param workflow_manager: Classe adaptadora para o Step Functions.
        """
        self.workflow_manager = workflow_manager

    def start_workflow(self, state_machine_arn: str, input_data: dict):
        """
        Inicia a execução de um fluxo de trabalho no Step Functions.
        :param state_machine_arn: ARN da máquina de estados.
        :param input_data: Dados de entrada para a execução.
        :return: ARN da execução do fluxo de trabalho.
        """
        return self.workflow_manager.start_execution(
            state_machine_arn, input_data
        )
