import pytest

from selene import browser, Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

@pytest.fixture(scope='function')
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'
    # browser.config.hold_driver_at_exit = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser_version = '100.0'
    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': browser_version,
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor='https://user1:1234@selenoid.autotests.cloud/wd/hub',
        options=options
    )
    browser_ = Browser(Config(driver))

    yield browser_

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()