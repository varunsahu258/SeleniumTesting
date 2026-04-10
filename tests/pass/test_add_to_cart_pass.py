"""
test_add_to_cart_pass.py
------------------------
PASS test: Adds a product to the cart on SauceDemo and verifies
the cart badge count increments to 1.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.pass_test
def test_add_to_cart_pass(driver):
    """Login, add the first product to cart, confirm badge shows 1."""

    # ── Login ─────────────────────────────────────────────────────────────────
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    # ── Add the first "Add to cart" button product ────────────────────────────
    add_btn = driver.find_element(
        By.CSS_SELECTOR, ".inventory_item:first-child button.btn_inventory"
    )
    add_btn.click()

    # ── Wait for badge to appear and check count ──────────────────────────────
    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
    )

    # ── Assertions ────────────────────────────────────────────────────────────
    assert badge.is_displayed(), "Cart badge must be visible after adding item"
    assert badge.text == "1", f"Cart badge should read '1', got '{badge.text}'"

    # Confirm button text changed to "Remove"
    remove_btn = driver.find_element(
        By.CSS_SELECTOR, ".inventory_item:first-child button.btn_inventory"
    )
    assert remove_btn.text == "Remove", (
        f"Button should read 'Remove' after adding, got '{remove_btn.text}'"
    )
