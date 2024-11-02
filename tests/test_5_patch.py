"""
TESTS FOR THE PATCH OPERATION
Author: Chinmay Mudholkar
Date: 04/2024
"""

import json

import pytest

from config.constants import api_response_codes
from libs import *
from libs import api_ops, config_ops


class Test_Patch:
    config = config_ops.config_operations()
    api = api_ops.api_operations()

    @pytest.mark.order(501)
    @pytest.mark.patch
    def test_patch_001(self):
        _expected = get_current_date_time().split(sep="T")[0]
        _params = {"name": "morpheus", "job": "zion resident"}
        _endpoint = f"{self.config.get_base_url()}/api/users/2"
        _response = self.api.api_patch(endpoint=_endpoint, params=_params)
        assert _response.status_code == api_response_codes.OK, "Invalid response code"
        _response_json = json.loads(_response.text)
        _actual = _response_json["updatedAt"]
        _actual = _actual.split(sep="T")[0]  # Don't verify the time
        assert (
            _expected == _actual
        ), f"Incorrect data in response.  Expected {_expected}, actual {_actual}."
