"""
TESTS FOR THE POST OPERATION
Author: Chinmay Mudholkar
Date: 04/2024
"""

import pytest
import json
from libs import config_ops
from libs import api_ops
from config.constants import api_response_codes


class Test_Post:
    config = config_ops.config_operations()
    api = api_ops.api_operations()

    @pytest.mark.order(201)
    @pytest.mark.post
    def test_post_001(self):
        _expected_id = 4
        _endpoint = f"{self.config.get_base_url()}/api/register"
        _request_body = {"email": "eve.holt@reqres.in", "password": "pistol"}
        _response = self.api.api_post(endpoint=_endpoint, body=_request_body)
        assert _response.status_code == api_response_codes.OK, "Invalid response code"
        _response_json = json.loads(_response.text)
        assert (
            _response_json["id"] == _expected_id
        ), f"Invalid response content.  Expected ID {_expected_id}, received {_response_json['id']}"
