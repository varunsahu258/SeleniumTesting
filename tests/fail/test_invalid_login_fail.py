"""
test_invalid_login_fail.py
--------------------------
FAIL test: Submits completely empty credentials and then wrongly asserts
that no error is shown — intentional failure.
"""

import pytest
from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.fail_test
def test_invalid_login_fail(driver):
    """
    INTENTIONAL FAILURE:
    Clicks login with empty fields, then asserts the error container is NOT
    displayed — which is wrong; an error always appears for empty submission.
    """
    driver.get(BASE_URL)

    # ── Submit with blank username and password ────────────────────────────────
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")

    # ── Wrong assertion — error IS shown, so this will fail ───────────────────
    assert not error.is_displayed(), (
        "[EXPECTED FAILURE] Error SHOULD appear for empty login, "
        "but we asserted it should not."
    )
