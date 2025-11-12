import pytest
from libs.logging_config import get_logger

_logger = get_logger("tests")

@pytest.fixture(scope="session", autouse=True)
def session_logger():
    _logger.info("Test session starting")
    yield
    _logger.info("Test session finished")


@pytest.fixture(autouse=True)
def log_test_start_and_end(request):
    _logger.info("START TEST: %s", request.node.name)
    try:
        yield
    except Exception:
        # Log exception with full stacktrace then re-raise so pytest also reports it
        _logger.exception("EXCEPTION in test: %s", request.node.name)
        raise
    finally:
        _logger.info("END TEST: %s", request.node.name)
