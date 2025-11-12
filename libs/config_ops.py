"""
THIS CLASS DEFINES THE FUNCTIONS TO GET VALUES FROM THE CONFIGURATION FILE
Author: Chinmay Mudholkar
Date: 04/2024
"""

import os
import configparser

from config.constants import ConfigSections
from libs.logging_config import get_logger

_logger = get_logger(__name__)


class config_operations:
    config = configparser.RawConfigParser()
    config.read(filenames="config/config.ini")

    def get_current_environment(self) -> str:
        val = self.config.get(ConfigSections.COMMON, "environment")
        _logger.debug("get_current_environment -> %s", val)
        return val

    def get_project_name(self) -> str:
        val = self.config.get(ConfigSections.COMMON, "project_name")
        _logger.debug("get_project_name -> %s", val)
        return val

    def get_base_url(self) -> str:
        val = self.config.get(
            ConfigSections.BASE_URLS, self.get_current_environment()
        )
        _logger.debug("get_base_url -> %s", val)
        return val

    def get_api_key(self) -> str:
        """Return API key value.

        Priority:
        1. Environment variable REQRES_API_KEY
        2. Environment variable API_KEY
        3. config/config.ini value

        For security we avoid logging the raw API key value — only the source.
        """
        env_key = os.environ.get("REQRES_API_KEY") or os.environ.get("API_KEY")
        if env_key:
            _logger.debug("get_api_key -> source=env")
            return env_key

        # fallback to config
        try:
            val = self.config.get(ConfigSections.COMMON, "api_key")
            _logger.debug("get_api_key -> source=config")
            return val
        except Exception:
            _logger.debug("get_api_key -> source=none")
            return ""
