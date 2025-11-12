"""
TESTS FOR THE DELETE OPERATION
Author: Chinmay Mudholkar
Date: 04/2024
"""

import pytest
import requests

from config.constants import ApiResponseCodes
from libs import api_ops, config_ops


class TestDelete:
    config = config_ops.config_operations()
    api = api_ops.ApiOperations()

    @pytest.mark.delete
    def test_delete_001(self):
        _endpoint = f"{self.config.get_base_url()}/api/users/2"
        _response = self.api.api_delete(endpoint=_endpoint)
        # assert (
        #         _response.status_code == ApiResponseCodes.NO_CONTENT
        # ), "Invalid response code"
        assert _response.status_code == ApiResponseCodes.NO_CONTENT, (
            f"Invalid response code. Expecting {ApiResponseCodes.NO_CONTENT}, received {_response.status_code}."
        )
        assert _response.text == "" or _response.content == b"", "Expected no response body for 204"

