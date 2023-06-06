import pytest
from selene import browser
from selene.support.shared import config


# def browser_setup():
#     browser.open('https://google.com')
#     browser.config.window_width = 1200
#     browser.config.window_height = 800
#     config.headers = {
#         'Accept-Language': 'en-US,en;q=0.9',
#     }

@pytest.fixture(autouse = True)
def setup_browser():
    config.timeout = 10
    config.window_width = 1920
    config.window_height = 1080
    config.base_url = 'https://www.google.com'

    yield