"""
THIS MODULE CONTAINS SEVERAL WRAPPER FUNCTIONS THAT ARE USUALLY REQUIRED IN ANY AUTOMATION FRAMEWORK
Author: Chinmay Mudholkar
Date: 04/2024
"""

import base64
import os
import random
import string
import time
import uuid
from datetime import datetime, timezone

from config.constants import FileEncoding
from libs.config_ops import config_operations
from libs.logging_config import get_logger

_logger = get_logger(__name__)

# Create a shared config_operations instance for module-level helpers
_config = config_operations()


def get_project_root() -> str:
    _pr = os.path.dirname(__file__)
    while os.path.basename(_pr.upper()) != _config.get_project_name().upper():
        _pr = os.path.dirname(_pr)
    _logger.debug("get_project_root -> %s", _pr)
    return _pr


def get_new_uuid() -> str:
    val = str(uuid.uuid4())
    _logger.debug("get_new_uuid -> %s", val)
    return val


def get_random_number(length: int = 16) -> str:
    val = "".join(random.choices(string.digits, k=length))
    _logger.debug("get_random_number(length=%s) -> %s", length, val)
    return val


def convert_time_units_to_seconds(time_unit: str) -> int:
    _seconds = 0
    if time_unit[-1].lower() == "m":
        _seconds = int(time_unit[0:-1]) * 60
    elif time_unit[-1].lower() == "h":
        _seconds = int(time_unit[0:-1]) * 60 * 60
    else:
        _seconds = int(time_unit.lower().replace("s", ""))
    _logger.debug("convert_time_units_to_seconds(%s) -> %s", time_unit, _seconds)
    return _seconds


def wait(timeout: str) -> None:
    _seconds = convert_time_units_to_seconds(time_unit=timeout)
    _logger.debug("wait(%s) sleeping for %s seconds", timeout, _seconds)
    time.sleep(_seconds)


def get_current_date_time():
    val = datetime.now(timezone.utc).strftime("%FT%T")
    _logger.debug("get_current_date_time -> %s", val)
    return val


def get_base64_encoded_string(text: str) -> str:
    text_bytes = text.encode(encoding=FileEncoding.ASCII)
    val = base64.b64encode(text_bytes).decode(encoding=FileEncoding.ASCII)
    _logger.debug("get_base64_encoded_string -> %s", val)
    return val


def get_base64_decoded_string(encoded_string: str) -> str:
    base64_bytes = encoded_string.encode(encoding=FileEncoding.ASCII)
    val = base64.b64decode(base64_bytes).decode(encoding=FileEncoding.ASCII)
    _logger.debug("get_base64_decoded_string -> %s", val)
    return val
