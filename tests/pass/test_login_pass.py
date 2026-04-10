"""
test_login_pass.py
------------------
PASS test: Valid login on SauceDemo.
Verifies successful authentication redirects to /inventory.html
and that the page title is visible.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.pass_test
def test_login_pass(driver):
    """Login with valid standard_user credentials — must land on inventory page."""
    driver.get(BASE_URL)

    # ── Enter credentials ──────────────────────────────────────────────────────
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # ── Wait for inventory page to load ────────────────────────────────────────
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    # ── Assertions ─────────────────────────────────────────────────────────────
    assert "inventory.html" in driver.current_url, (
        f"Expected inventory URL, got: {driver.current_url}"
    )

    # The primary app logo must be visible after login
    logo = driver.find_element(By.CSS_SELECTOR, ".app_logo")
    assert logo.is_displayed(), "App logo should be visible after login"
    assert logo.text == "Swag Labs", f"Unexpected logo text: {logo.text}"
