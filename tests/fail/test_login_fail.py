"""
test_login_fail.py
------------------
FAIL test: Intentionally uses WRONG password for login.
Asserts a URL it will never reach — test must fail.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.fail_test
def test_login_fail(driver):
    """
    INTENTIONAL FAILURE:
    Uses an incorrect password; then asserts we are on the inventory page.
    The assertion will fail because login is rejected.
    """
    driver.get(BASE_URL)

    # ── Enter WRONG credentials ────────────────────────────────────────────────
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("WRONG_PASSWORD")   # ← wrong
    driver.find_element(By.ID, "login-button").click()

    # ── Assertion will fail — still on login page, not inventory ──────────────
    assert "inventory.html" in driver.current_url, (
        f"[EXPECTED FAILURE] Should NOT reach inventory with bad credentials. "
        f"Current URL: {driver.current_url}"
    )
