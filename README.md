# PyApiBasics

## Overview
PyApiBasics is a lightweight API test automation framework written in Python using PyTest. It provides a small, opinionated test harness and example tests that demonstrate common HTTP operations (GET, POST, PUT, PATCH, DELETE) against a REST API. The project is intended as a starting point for building automated API test suites.

Key features
- Simple utilities for common tasks (date/time helpers, base64 helpers, UUIDs) in `libs`.
- A compact `ApiOperations` helper in `libs/api_ops.py` for making HTTP requests and handling common logging/serialization concerns.
- Centralized configuration in `config/config.ini` and small helper in `libs/config_ops.py`.
- Centralized logging to a root-level `automation.log` with rotation and automatic redaction of sensitive values.
- A deterministic test mode (tests mock HTTP) so local runs are reliable and repeatable.

## Project layout
- `libs/` - library code used by tests (api operations, config helpers, common utilities, logging config).
- `config/` - configuration files (e.g. `config.ini`).
- `tests/` - pytest test cases and `conftest.py` fixtures.

## How it works (high-level)
1. Tests import helpers from `libs` and read configuration from `config/config.ini` via `libs/config_ops.py`.
2. `ApiOperations` builds and issues HTTP requests using `requests.Session`. By default it attaches the configured API key as the `x-api-key` header.
3. Logging is centralized in `libs/logging_config.py`. All modules use `get_logger(__name__)` to obtain a child logger under the project logger `PyApiBasics`.
4. Logs are written to `automation.log` at the repository root using a rotating file handler, and sensitive fields (API keys, tokens, passwords, email addresses) are redacted automatically before writing.
5. During test runs, `tests/conftest.py` can run a session-scoped fixture that monkeypatches `requests.Session.request` to return canned responses for the sample tests — this makes test runs deterministic and avoids reliance on external services.

## Installation
Requirements: Python 3.10 or newer.

1. Clone the repository:

```bash
git clone https://github.com/chinmaymudholkar/PyApiBasics.git
cd PyApiBasics
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Verify setup (run only the setup checks):

```bash
pytest -m setup -q
```

## Configuration
Primary configuration is stored in `config/config.ini`.

Example `config/config.ini` values used by the framework:

```ini
[common]
project_name = PYAPIBASICS
environment = TEST
api_key = reqres-free-v1

[base_urls]
TEST = https://reqres.in
```

- `api_key`: A generic API key (default: `reqres-free-v1`) will be attached automatically to requests as the `x-api-key` header by `ApiOperations`.
- Environment override: you can set the API key via environment variables `REQRES_API_KEY` or `API_KEY`. `libs/config_ops.get_api_key()` gives priority to `REQRES_API_KEY`, then `API_KEY`, then the `config.ini` value. For security prefer environment variables or secret stores for production.

## Centralized logging
- Log file: `automation.log` in the project root.
- Implemented in `libs/logging_config.py` as a centralized `PyApiBasics` logger. Child loggers are created with `get_logger(__name__)`.
- Log rotation: a `RotatingFileHandler` is configured with `maxBytes=5*1024*1024` and `backupCount=5`.
- Redaction: the logger masks sensitive keys (default set includes `authorization`, `x-api-key`, `api_key`, `password`, `token`, `access_token`, `email`) when logging headers or bodies. The redact behavior can be adjusted in `libs/logging_config.py` by modifying `SENSITIVE_KEYS` or the `redact()` helper.

## Tests
- Test files live in `tests/` and use pytest markers: `setup`, `get`, `post`, `delete`, `put`, `patch`.
- The test suite includes a `tests/conftest.py` file that provides useful fixtures:
  - A session-scoped autouse fixture that (by default in this repo) monkeypatches `requests.Session.request` to return canned responses for the sample tests. This yields deterministic tests that do not depend on the network.
  - An autouse fixture that logs every test START and END and logs exception stacktraces when tests fail.

Running tests

- Run all tests:

```bash
pytest -q
```

- Toggle request mocking (deterministic tests) via environment variable `USE_MOCK_REQUESTS`:

```bash
# default (mocking enabled)
export USE_MOCK_REQUESTS=true
pytest -q

# disable mocking -> tests will make real HTTP requests
export USE_MOCK_REQUESTS=false
pytest -q
```

- Run tests for a specific marker, for example GET tests:

```bash
pytest -m get -q
```

- Re-run a failing test (verbose output):

```bash
pytest tests/test_1_get.py::Test_Get::test_get_002 -q -r a
```

View logs

- Tail the log while running tests:

```bash
tail -f automation.log
```

- Show last N lines:

```bash
tail -n 200 automation.log
```

## Notes on external API usage vs deterministic mode
- The real `reqres.in` API may require an API key or change behavior. To avoid flakiness and to make local development fast and repeatable, the repository's tests are set up to run in deterministic mode (see the `_mock_requests` fixture in `tests/conftest.py`).
- To exercise the real API:
  - Remove or edit the `_mock_requests` fixture in `tests/conftest.py` (it is session-scoped). After removal the tests will make real HTTP requests.
  - Ensure the `api_key` in `config/config.ini` is set to a valid value or modify `libs/config_ops.py` to read the key from an environment variable.

## Customization & extension points
- Add or change redacted keys: edit `SENSITIVE_KEYS` in `libs/logging_config.py`.
- Adjust rotation size/retention: modify `RotatingFileHandler` settings in `libs/logging_config.py`.
- Toggle deterministic tests: modify or gate the `_mock_requests` fixture in `tests/conftest.py` (e.g. based on an environment variable).
- Move API key to environment: change `libs/config_ops.py` to prefer `os.environ.get("API_KEY")` and update README with instructions.

## Troubleshooting
- If tests fail with 401/Unauthorized during a live run, check that `config/config.ini` or your environment contains a valid API key and consider running in the deterministic mocked mode for development.
- Use `automation.log` to inspect detailed request/response logs and stacktraces for failures. Sensitive values will be redacted.

## Contribution & License
Contributions welcome — open an issue or PR with improvements. See `LICENSE` for license terms.