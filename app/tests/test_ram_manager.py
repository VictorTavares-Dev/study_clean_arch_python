import pytest
from unittest.mock import patch, MagicMock
from src.adapter.ram_manager import RAMAdapter


@pytest.fixture
def mock_boto3_client():
    with patch("src.adapter.ram_manager.boto3.client") as mock_client:
        yield mock_client


def test_init_with_credentials(mock_boto3_client):
    credentials = {
        "AccessKeyId": "AKIA...",
        "SecretAccessKey": "SECRET",
        "SessionToken": "TOKEN",
    }
    adapter = RAMAdapter(credentials=credentials, region_name="us-west-2")
    mock_boto3_client.assert_called_with(
        "ram",
        region_name="us-west-2",
        aws_access_key_id="AKIA...",
        aws_secret_access_key="SECRET",
        aws_session_token="TOKEN",
    )
    assert adapter.credentials == credentials


def test_init_without_credentials(mock_boto3_client):
    adapter = RAMAdapter(region_name="us-east-1")
    mock_boto3_client.assert_called_with("ram", region_name="us-east-1")
    assert not hasattr(adapter, "credentials")


def test_get_pagination_returns_paginator(mock_boto3_client):
    mock_paginator = MagicMock()
    mock_boto3_client.return_value.get_paginator.return_value = mock_paginator
    adapter = RAMAdapter(region_name="us-east-1")
    paginator = adapter.get_pagination("list_resources")
    adapter._RAMAdapter__ram_client.get_paginator.assert_called_with(
        "list_resources"
    )
    assert paginator == mock_paginator


@patch("botocore.client.BaseClient._make_api_call", autospec=True)
def test_get_resource_shares(mock_api_call, mock_make_api_call_fixture):
    mock_api_call.side_effect = mock_make_api_call_fixture
    adapter = RAMAdapter(region_name="us-east-1")
    response = adapter.get_resource_shares("OTHER-ACCOUNTS")
    assert len(response["resourceShares"]) == 1


@patch("botocore.client.BaseClient._make_api_call", autospec=True)
def test_list_resource_share_permissions(
    mock_api_call, mock_make_api_call_fixture
):
    mock_api_call.side_effect = mock_make_api_call_fixture
    adapter = RAMAdapter(region_name="us-east-1")
    response = adapter.list_resource_share_permissions(
        resource_share_arn="arn:aws:ram:us-east-1:888577041900:resource-share/8901c2d9-77f5-4f0a-803d-419c6408778c"
    )
    assert len(response["permissions"]) == 3


"""
O parâmetro autospec=True no decorator @patch faz com que o mock criado tenha a
mesma assinatura (parâmetros) do método original que está sendo substituído. Ou
seja, o mock só aceitará os mesmos argumentos que o método real.

No seu caso, o método BaseClient._make_api_call espera três argumentos: self,
operation_name e kwargs. Sem autospec=True, o mock criado pelo patch aceita
qualquer chamada de argumentos, o que pode causar problemas quando o código
espera um método de instância (com self). Com autospec=True, o mock exige que a
chamada siga exatamente a assinatura do método original, incluindo o self.

O teste só funciona com autospec=True porque o código do boto3 chama
_make_api_call como método de instância, passando self automaticamente. Se o
mock não estiver preparado para receber self (ou seja, se não tiver a
assinatura correta), ocorre um erro de argumentos faltando, como você viu
anteriormente.

Resumindo:

- autospec=True garante que o mock tem a mesma assinatura do método original.
- Isso evita erros de chamada e garante que o mock funcione corretamente em
métodos de instância.
"""
