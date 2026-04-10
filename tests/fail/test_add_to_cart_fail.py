"""
test_add_to_cart_fail.py
------------------------
FAIL test: Adds one product but incorrectly asserts the badge shows "2".
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.fail_test
def test_add_to_cart_fail(driver):
    """
    INTENTIONAL FAILURE:
    Only one item is added, but we assert badge count equals '2'.
    """

    # ── Login ─────────────────────────────────────────────────────────────────
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    # ── Add only ONE item ─────────────────────────────────────────────────────
    add_btn = driver.find_element(
        By.CSS_SELECTOR, ".inventory_item:first-child button.btn_inventory"
    )
    add_btn.click()

    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
    )

    # ── Wrong assertion: expects 2 items when only 1 was added ────────────────
    assert badge.text == "2", (
        f"[EXPECTED FAILURE] Badge is '1' but we asserted '2'. Got: '{badge.text}'"
    )
