"""
VARIOUS TESTS FOR THE GET OPERATION
Author: Chinmay Mudholkar
Date: 04/2024
"""

import pytest
import json
from libs import config_ops
from libs import api_ops
from config.constants import api_response_codes


class Test_Get:
    config = config_ops.config_operations()
    api = api_ops.api_operations()

    @pytest.mark.order(101)
    @pytest.mark.get
    def test_get_001(self):
        _endpoint = self.config.get_base_url()
        _response = self.api.api_get(endpoint=_endpoint)
        assert (
            _response.status_code == api_response_codes.OK
        ), f"Invalid response code.  Expecting {api_response_codes.OK}, received {_response.status_code}."

    @pytest.mark.order(102)
    @pytest.mark.get
    def test_get_002(self):
        _expected_fn = "Janet"
        _endpoint = f"{self.config.get_base_url()}/api/users/2"
        _response = self.api.api_get(endpoint=_endpoint)
        assert (
            _response.status_code == api_response_codes.OK
        ), f"Invalid response code.  Expecting {api_response_codes.OK}, received {_response.status_code}."
        _response_json = json.loads(_response.text)
        _actual = _response_json["data"]["first_name"]
        assert (
            _expected_fn == _actual
        ), f"Incorrect data in response.  Expected {_expected_fn}, actual {_actual}."

    @pytest.mark.order(103)
    @pytest.mark.get
    def test_get_003(self):
        _endpoint = f"{self.config.get_base_url()}/api/users/23"
        _response = self.api.api_get(endpoint=_endpoint)
        assert (
            _response.status_code == api_response_codes.NOT_FOUND
        ), f"Invalid response code.  Expecting {api_response_codes.NOT_FOUND}, received {_response.status_code}."
