"""
conftest.py — Shared Pytest fixtures for the entire test suite.
Provides a headless Chrome WebDriver instance with sensible defaults.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


def pytest_configure(config):
    """Register custom markers to avoid PytestUnknownMarkWarning."""
    config.addinivalue_line("markers", "pass_test: marks tests expected to pass")
    config.addinivalue_line("markers", "fail_test: marks tests expected to fail (intentional)")


@pytest.fixture(scope="function")
def driver():
    """
    Yields a configured Chrome WebDriver for each test function.
    Uses headless mode so tests run in CI/CD without a display.
    Quits the driver after each test automatically.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")          # No GUI
    chrome_options.add_argument("--no-sandbox")         # Required in some Linux envs
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")

    # ChromeDriver must be on PATH (or pass executable_path via Service)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)   # Global implicit wait — 10 seconds
    driver.maximize_window()

    yield driver
    time.sleep(3)
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    """
    Returns a WebDriverWait instance (explicit waits, 15-second timeout).
    Use alongside driver fixture for fine-grained element waits.
    """
    return WebDriverWait(driver, 15)
