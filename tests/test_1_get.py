"""
VARIOUS TESTS FOR THE GET OPERATION
Author: Chinmay Mudholkar
Date: 04/2024
"""

import json

import pytest
from urllib3.exceptions import HTTPError

from config.constants import ApiResponseCodes
from libs import api_ops, config_ops
import requests


class TestGet:
    config = config_ops.config_operations()
    api = api_ops.ApiOperations()

    @pytest.mark.get
    def test_get_001(self):
        _endpoint = self.config.get_base_url()
        _response = self.api.api_get(endpoint=_endpoint)
        _response.raise_for_status()


    @pytest.mark.get
    def test_get_002(self):
        _expected = "Janet"
        _endpoint = f"{self.config.get_base_url()}/api/users/2"
        _response = self.api.api_get(endpoint=_endpoint)
        _response.raise_for_status()
        _response_json = json.loads(_response.text)
        _actual = _response_json["data"]["first_name"]
        assert (
            _expected == _actual
        ), f"Incorrect data in response.  Expected {_expected}, actual {_actual}."


    @pytest.mark.get
    def test_get_003(self):
        _endpoint = f"{self.config.get_base_url()}/api/users/123" # Non-existent user
        _response = self.api.api_get(endpoint=_endpoint)
        with pytest.raises(requests.exceptions.HTTPError):
            _response.raise_for_status()
