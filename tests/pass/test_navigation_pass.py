"""
test_navigation_pass.py
-----------------------
PASS test: Navigates from inventory to product detail page and back
using SauceDemo. Verifies URL and key elements at each step.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.pass_test
def test_navigation_pass(driver):
    """
    1. Login → inventory page
    2. Click first product name → product detail page
    3. Click Back to Products → back to inventory
    """

    # ── Login ─────────────────────────────────────────────────────────────────
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    assert "inventory.html" in driver.current_url

    # ── Navigate to first product's detail page ────────────────────────────────
    first_product_link = driver.find_element(
        By.CSS_SELECTOR, ".inventory_item:first-child .inventory_item_name"
    )
    product_name = first_product_link.text
    first_product_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains("inventory-item"))

    # Detail page assertions
    assert "inventory-item" in driver.current_url, (
        f"Expected detail page URL, got: {driver.current_url}"
    )
    detail_name = driver.find_element(By.CSS_SELECTOR, ".inventory_details_name")
    assert detail_name.is_displayed(), "Product name must be visible on detail page"
    assert detail_name.text == product_name, (
        f"Detail page name '{detail_name.text}' != inventory name '{product_name}'"
    )

    # ── Navigate back to inventory ─────────────────────────────────────────────
    driver.find_element(By.ID, "back-to-products").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))

    assert "inventory.html" in driver.current_url, "Should return to inventory page"
    products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
    assert len(products) == 6, f"Inventory should still have 6 products, got {len(products)}"
