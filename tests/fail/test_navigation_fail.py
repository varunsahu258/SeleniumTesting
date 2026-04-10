"""
test_navigation_fail.py
-----------------------
FAIL test: Navigates to the inventory page but asserts the wrong URL fragment.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.fail_test
def test_navigation_fail(driver):
    """
    INTENTIONAL FAILURE:
    After login, asserts URL contains 'checkout' instead of 'inventory'.
    """

    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    # ── Wrong URL assertion ───────────────────────────────────────────────────
    assert "checkout" in driver.current_url, (
        f"[EXPECTED FAILURE] URL should contain 'checkout' but got: {driver.current_url}"
    )
