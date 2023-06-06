import pytest
from selene.support.shared import config

@pytest.fixture(autouse = True)
def setup_browser():
    config.timeout = 10
    config.window_width = 1920
    config.window_height = 1080
    config.base_url = 'https://www.google.com/ncr'

    yield