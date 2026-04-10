"""
test_logout_fail.py
-------------------
FAIL test: Tries to click the logout link WITHOUT opening the sidebar menu first.
The element is hidden and click will raise an exception / NoSuchElementException.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.fail_test
def test_logout_fail(driver):
    """
    INTENTIONAL FAILURE:
    Skips opening the burger menu and attempts to click the hidden logout link.
    Selenium will raise an ElementNotInteractableError (or similar),
    causing the test to fail.
    """
    driver.get(BASE_URL)

    # ── Login ─────────────────────────────────────────────────────────────────
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    # ── Intentional mistake: click logout without opening the menu ─────────────
    # The link exists in DOM but is NOT visible — click will fail
    driver.find_element(By.ID, "logout_sidebar_link").click()

    # This assertion is never reached; the click above raises an exception
    assert "saucedemo.com" not in driver.current_url, "Should have logged out"
