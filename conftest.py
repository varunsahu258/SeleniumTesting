"""
conftest.py — Shared Pytest fixtures for the entire test suite.
Provides a visible Chrome WebDriver instance with slowed-down actions for demo purposes.
"""

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

# ── Slow-motion patch ────────────────────────────────────────────────────────
original_click = webdriver.remote.webelement.WebElement.click
original_send_keys = webdriver.remote.webelement.WebElement.send_keys

def slow_click(self):
    original_click(self)
    time.sleep(1.5)        # pause after every click

def slow_send_keys(self, *args):
    original_send_keys(self, *args)
    time.sleep(1.5)        # pause after every keystroke

webdriver.remote.webelement.WebElement.click = slow_click
webdriver.remote.webelement.WebElement.send_keys = slow_send_keys
# ─────────────────────────────────────────────────────────────────────────────


def pytest_configure(config):
    """Register custom markers to avoid PytestUnknownMarkWarning."""
    config.addinivalue_line("markers", "pass_test: marks tests expected to pass")
    config.addinivalue_line("markers", "fail_test: marks tests expected to fail (intentional)")


@pytest.fixture(scope="function")
def driver():
    """
    Yields a configured Chrome WebDriver for each test function.
    Runs in visual (headed) mode so you can watch every action.
    Quits the driver after each test automatically.
    """
    chrome_options = Options()
    # chrome_options.add_argument("--headless")       # commented out = visual mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)   # Global implicit wait — 10 seconds
    driver.maximize_window()

    yield driver

    time.sleep(3)        # pause at the end so you can see the final state
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    """
    Returns a WebDriverWait instance (explicit waits, 15-second timeout).
    Use alongside driver fixture for fine-grained element waits.
    """
    return WebDriverWait(driver, 15)
