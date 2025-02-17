import json
from src.adapters.credentials_manager import CredentialsManager
from src.adapters.db_nosql_manager import NoSQLDBManager
from src.adapters.queue_manager import QueueManager
from src.adapters.workflow_manager import WorkflowManager
from src.use_cases.manage_credentials import ManageCredentials
from src.use_cases.manage_nosql_db import ManageNoSQLDatabase
from src.use_cases.manage_queue import ManageQueue
from src.use_cases.manage_workflow import ManageWorkflows


def lambda_handler(event, context):
    # Inicialização dos adaptadores
    sts_manager = CredentialsManager()
    dynamodb_manager = NoSQLDBManager(table_name="MyDynamoDBTable")
    sqs_manager = QueueManager(
        queue_url="https://sqs.us-east-1.amazonaws.com/123456789012/my-queue"
    )
    step_functions_manager = WorkflowManager()

    # Caso de uso de credenciais (STS)
    manage_credentials = ManageCredentials(sts_manager)
    role_arn = "arn:aws:iam::123456789012:role/MyRole"
    session_name = "MySession"

    # Obter credenciais temporárias
    access_key, secret_key, session_token = (
        manage_credentials.get_temporary_credentials(role_arn, session_name)
    )
    print(f"Credenciais temporárias obtidas: {access_key}, {secret_key}")

    # Caso de uso para banco de dados NoSQL (DynamoDB)
    manage_nosql_db = ManageNoSQLDatabase(dynamodb_manager)
    item_data = {
        "id": "123",
        "name": "Test Item",
        "description": "This is a test item",
    }

    # Salvar item no DynamoDB
    manage_nosql_db.save_item(item_data)

    # Caso de uso de filas SQS
    manage_sqs = ManageQueue(sqs_manager)
    message_body = json.dumps({"task": "Process data", "status": "Pending"})

    # Enviar mensagem para SQS
    manage_sqs.send_message(message_body)

    # Caso de uso para workflows (Step Functions)
    manage_workflows = ManageWorkflows(step_functions_manager)
    state_machine_arn = (
        "arn:aws:states:us-east-1:123456789012:stateMachine:MyStateMachine"
    )
    workflow_input = {"inputKey": "inputValue"}

    # Iniciar execução no Step Functions
    execution_arn = manage_workflows.start_workflow(
        state_machine_arn, workflow_input
    )
    print(f"Workflow iniciado com ARN de execução: {execution_arn}")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Processo concluído com sucesso!",
                "execution_arn": execution_arn,
            }
        ),
    }
