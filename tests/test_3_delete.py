"""
TESTS FOR THE DELETE OPERATION
Author: Chinmay Mudholkar
Date: 04/2024
"""

import pytest

from config.constants import api_response_codes
from libs import api_ops, config_ops


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
