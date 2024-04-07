"""
THESE TESTS VERIFY THE FRAMEWORK IS SETUP CORRECTLY AND ARE EXECUTED BEFORE ALL OTHER TESTS
Author: Chinmay Mudholkar
Date: 04/2024
"""

import pytest
from libs import config_ops
import sys
from libs import *


class Test_Get:
    config = config_ops.config_operations()

    @pytest.mark.order(1)
    @pytest.mark.setup
    def test_setup_001(self):
        _expected = 3.10
        _actual = float(".".join(sys.version.split(sep=" ")[0].split(sep=".")[:2]))
        assert _actual >= _expected, "Invalid Python version"

    @pytest.mark.order(2)
    @pytest.mark.setup
    def test_setup_002(self):
        _expected = "PYAPIBASICS"
        _actual = self.config.get_project_name()
        wait(timeout="3s")  # Just showing off :)
        assert _expected == _actual, "Could not find the config file."
