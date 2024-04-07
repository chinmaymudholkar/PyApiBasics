"""
TESTS FOR THE DELETE OPERATION
Author: Chinmay Mudholkar
Date: 04/2024
"""

import pytest
from libs import config_ops
from libs import api_ops
from config.constants import api_response_codes


class Test_Delete:
    config = config_ops.config_operations()
    api = api_ops.api_operations()

    @pytest.mark.order(301)
    @pytest.mark.delete
    def test_delete_001(self):
        _endpoint = f"{self.config.get_base_url()}/api/users/2"
        _response = self.api.api_delete(endpoint=_endpoint)
        assert (
            _response.status_code == api_response_codes.NO_CONTENT
        ), "Invalid response code"
