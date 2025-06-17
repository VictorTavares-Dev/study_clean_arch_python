import pytest
import botocore
from constants import RESPONSE_PERMISSIONS, RESPONSE_GET_RESOURCE_SHARES


def mock_make_api_call(self, operation_name, kwargs):
    orig = botocore.client.BaseClient._make_api_call
    if operation_name == "GetResourceShares":
        return {
            "resourceShares": RESPONSE_GET_RESOURCE_SHARES
        }
    elif operation_name == "ListResourceSharePermissions":
        resource_share_arn = kwargs.get("resourceShareArn")
        return {
            "permissions": RESPONSE_PERMISSIONS.get(resource_share_arn, [])
        }
    return orig(self, operation_name, kwargs)


@pytest.fixture
def mock_make_api_call_fixture():
    return mock_make_api_call
