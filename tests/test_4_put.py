"""
TESTS FOR THE PUT OPERATION
Author: Chinmay Mudholkar
Date: 04/2024
"""

import pytest
import json
from libs import config_ops
from libs import api_ops
from libs import *
from config.constants import api_response_codes


class Test_Put:
    config = config_ops.config_operations()
    api = api_ops.api_operations()

    @pytest.mark.order(401)
    @pytest.mark.put
    def test_put_001(self):
        _expected = get_current_date_time()
        _params = {"name": "morpheus", "job": "zion resident"}
        _endpoint = f"{self.config.get_base_url()}/api/users/2"
        _response = self.api.api_put(endpoint=_endpoint, params=_params)
        assert _response.status_code == api_response_codes.OK, "Invalid response code"
        _response_json = json.loads(_response.text)
        _actual = _response_json["updatedAt"]
        _actual = _actual.split(sep=".")[0]  # Don't verify the miliseconds
        assert (
            _expected == _actual
        ), f"Incorrect data in response.  Expected {_expected}, actual {_actual}."
