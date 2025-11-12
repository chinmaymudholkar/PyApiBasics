import logging
import os
from typing import Optional, Any
from logging.handlers import RotatingFileHandler
import json
import re

# Central logging configuration for the project.
# Creates a single logger named 'PyApiBasics' that writes to a root-level log file.

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_FILE = os.path.join(ROOT_DIR, "automation.log")

logger = logging.getLogger("PyApiBasics")

# Default sensitive keys to redact when logging headers/body
SENSITIVE_KEYS = {"authorization", "x-api-key", "api_key", "password", "token", "access_token", "email"}


class RedactingFormatter(logging.Formatter):
    """Formatter that redacts sensitive fields in the formatted message.

    It attempts to find JSON-like key/value pairs and masks known sensitive keys.
    """

    REDACT_RE = re.compile(r'(?P<key>"?\b(?:' + '|'.join(re.escape(k) for k in SENSITIVE_KEYS) + r')\b"?\s*[:=]\s*)("[^"]*"|\'[^\']*\'|[^,\}\]]+)', flags=re.IGNORECASE)

    def format(self, record: logging.LogRecord) -> str:
        s = super().format(record)
        try:
            # Replace detected sensitive values with "<redacted>" to avoid exposing secrets
            return self.REDACT_RE.sub(lambda m: m.group(1) + '"<redacted>"', s)
        except Exception:
            return s


def redact(obj: Any, keys: Optional[set] = None) -> str:
    """Serialize and redact sensitive keys from a dict/object for logging.

    Returns a string (JSON if possible) with sensitive values replaced by '<redacted>'.
    """
    if keys is None:
        keys = SENSITIVE_KEYS

    try:
        if isinstance(obj, dict):
            def _redact_dict(d):
                out = {}
                for k, v in d.items():
                    if isinstance(k, str) and k.lower() in keys:
                        out[k] = "<redacted>"
                    else:
                        # nested structures
                        if isinstance(v, dict):
                            out[k] = _redact_dict(v)
                        else:
                            out[k] = v
                return out

            redacted = _redact_dict(obj)
            return json.dumps(redacted, default=str)

        # For strings, try to redact JSON-like content
        if isinstance(obj, str):
            try:
                parsed = json.loads(obj)
                return redact(parsed, keys=keys)
            except Exception:
                # Fallback: regex replace key patterns
                s = obj
                # Replace occurrences like key=VALUE or "key": "VALUE"
                for key in keys:
                    s = re.sub(r'(?i)("?' + re.escape(key) + r'"?\s*[:=]\s*)("[^"]*"|\'[^\']*\'|[^,\}\]]+)', r'\1"<redacted>"', s)
                return s

        # Fallback: attempt json serialization
        return json.dumps(obj, default=str)
    except Exception:
        try:
            return repr(obj)
        except Exception:
            return "<unserializable>"


if not logger.handlers:
    # Rotating file handler
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5)
    formatter = RedactingFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
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
