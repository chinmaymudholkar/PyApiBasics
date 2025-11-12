from typing import Optional, Dict, Any
import json
import requests

from libs.config_ops import config_operations
from libs.logging_config import get_logger, redact

_logger = get_logger(__name__)
_config = config_operations()


class ApiOperations:
    """
    Lightweight helper for HTTP calls with optional redaction/logging.
    """

    def __init__(self, timeout: Optional[float] = 10.0, session: Optional[requests.Session] = None):
        self.timeout = timeout
        self.session = session or requests.Session()

    @staticmethod
    def _safe_serialize(obj: Any) -> str:
        try:
            return redact(obj)
        except Exception:
            try:
                return json.dumps(obj, default=repr)
            except Exception:
                try:
                    return repr(obj)
                except Exception:
                    return "<unserializable>"

    def _request(
        self,
        method: str,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> Optional[requests.Response]:
        # Build headers and include API key if present
        hdrs = dict(headers or {})
        if api_key := _config.get_api_key():
            hdrs.setdefault("x-api-key", api_key)

        kwargs: Dict[str, Any] = {}
        if hdrs:
            kwargs["headers"] = hdrs
        if params is not None:
            kwargs["params"] = params
        if body is not None:
            kwargs["json"] = body

        t = timeout or self.timeout
        _logger.debug(
            "HTTP start: %s %s headers=%s params=%s body=%s timeout=%s",
            method,
            endpoint,
            self._safe_serialize(hdrs),
            self._safe_serialize(params),
            self._safe_serialize(body),
            t,
        )

        try:
            resp = self.session.request(method=method, url=endpoint, timeout=t, **kwargs)
            body_preview = (resp.text or "")[:1000]
            _logger.info("HTTP complete: %s %s -> %s", method, endpoint, resp.status_code)
            _logger.debug("Response headers: %s", self._safe_serialize(dict(resp.headers or {})))
            _logger.debug("Response body (preview): %s", self._safe_serialize(body_preview))
            return resp
        except requests.RequestException:
            _logger.exception("HTTP request failed: %s %s", method, endpoint)
            return None

    def api_get(self, endpoint: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None):
        return self._request("GET", endpoint, headers=headers, params=params)

    def api_post(self, endpoint: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None, body: Optional[Dict[str, Any]] = None):
        return self._request("POST", endpoint, headers=headers, params=params, body=body)

    def api_put(self, endpoint: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None, body: Optional[Dict[str, Any]] = None):
        return self._request("PUT", endpoint, headers=headers, params=params, body=body)

    def api_patch(self, endpoint: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None, body: Optional[Dict[str, Any]] = None):
        return self._request("PATCH", endpoint, headers=headers, params=params, body=body)

    def api_delete(self, endpoint: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None, body: Optional[Dict[str, Any]] = None):
        return self._request("DELETE", endpoint, headers=headers, params=params, body=body)