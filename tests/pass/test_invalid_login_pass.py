"""
test_invalid_login_pass.py
--------------------------
PASS test: Confirms that an invalid login attempt correctly shows an error message.
Uses SauceDemo with a locked-out user.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.pass_test
def test_invalid_login_pass(driver):
    """
    Logs in with a locked-out account and verifies the error banner
    is displayed with the correct message.
    """
    driver.get(BASE_URL)

    # ── Attempt login with locked-out user ────────────────────────────────────
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # ── Wait for the error message container ─────────────────────────────────
    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    # ── Assertions ────────────────────────────────────────────────────────────
    assert error.is_displayed(), "Error message must be displayed for invalid login"
    assert "locked out" in error.text.lower(), (
        f"Expected 'locked out' in error text, got: '{error.text}'"
    )

    # Must still be on the login page
    assert "inventory" not in driver.current_url, (
        "Should NOT navigate away from login page on invalid credentials"
    )
