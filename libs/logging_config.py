import logging
import os
from typing import Optional

# Central logging configuration for the project.
# Creates a single logger named 'PyApiBasics' that writes to a root-level log file.

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_FILE = os.path.join(ROOT_DIR, "automation.log")

logger = logging.getLogger("PyApiBasics")

if not logger.handlers:
    # File handler writes all levels
    file_handler = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler for WARN+ to avoid noisy test output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.setLevel(logging.DEBUG)
    logger.propagate = False


def get_logger(name: Optional[str] = None):
    """Return a child logger under the project logger for a module or component.

    Usage:
        from libs.logging_config import get_logger
        _logger = get_logger(__name__)
    """
    if name:
        return logger.getChild(name)
    return logger

