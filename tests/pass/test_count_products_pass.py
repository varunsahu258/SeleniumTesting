"""
test_count_products_pass.py
---------------------------
PASS test: Verifies SauceDemo inventory shows exactly 6 products.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"
EXPECTED_PRODUCT_COUNT = 6


@pytest.mark.pass_test
def test_count_products_pass(driver):
    """After login, the inventory list must contain exactly 6 items."""

    # ── Login ─────────────────────────────────────────────────────────────────
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # ── Wait until all inventory cards are loaded ─────────────────────────────
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item"))
    )

    products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")

    # ── Assertions ────────────────────────────────────────────────────────────
    assert len(products) == EXPECTED_PRODUCT_COUNT, (
        f"Expected {EXPECTED_PRODUCT_COUNT} products, found {len(products)}"
    )

    # Every product card must have a name and a price
    for idx, product in enumerate(products):
        name = product.find_element(By.CSS_SELECTOR, ".inventory_item_name")
        price = product.find_element(By.CSS_SELECTOR, ".inventory_item_price")
        assert name.is_displayed(), f"Product {idx} name not visible"
        assert price.is_displayed(), f"Product {idx} price not visible"
        assert "$" in price.text, f"Price for product {idx} missing '$': {price.text}"
