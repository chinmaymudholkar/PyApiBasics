"""
THIS MODULE CONTAINS SEVERAL WRAPPER FUNCTIONS THAT ARE USUALLY REQUIRED IN ANY AUTOMATION FRAMEWORK
Author: Chinmay Mudholkar
Date: 04/2024
"""

import os
import uuid
import random
import string
import time
import base64
from config.constants import file_encoding
from datetime import datetime, timezone
from libs.config_ops import config_operations


def get_project_root() -> str:
    _pr = os.path.dirname(__file__)
    while os.path.basename(_pr.upper()) != config_operations.get_project_name().upper():
        _pr = os.path.dirname(_pr)
    return _pr


def get_new_uuid() -> str:
    return str(uuid.uuid4())


def get_random_number(length: int = 16) -> int:
    return "".join(random.choices(string.digits, k=length))


def convert_time_units_to_seconds(time_unit: str) -> int:
    _seconds = 0
    if time_unit[-1].lower() == "m":
        _seconds = int(time_unit[0:-1]) * 60
    elif time_unit[-1].lower() == "h":
        _seconds = int(time_unit[0:-1]) * 60 * 60
    else:
        _seconds = int(time_unit.lower().replace("s", ""))
    return _seconds


def wait(timeout: str) -> None:
    _seconds = convert_time_units_to_seconds(time_unit=timeout)
    time.sleep(_seconds)


def get_current_date_time():
    return datetime.now(timezone.utc).strftime("%FT%T")


def get_base64_encoded_string(text: str) -> str:
    text_bytes = text.encode(encoding=file_encoding.ASCII)
    return base64.b64encode(text_bytes).decode(encoding=file_encoding.ASCII)


def get_base64_decoded_string(encoded_string: str) -> str:
    base64_bytes = encoded_string.encode(encoding=file_encoding.ASCII)
    return base64.b64decode(base64_bytes).decode(encoding=file_encoding.ASCII)
