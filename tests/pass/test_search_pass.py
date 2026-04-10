"""
test_search_pass.py
-------------------
PASS test: OpenCart Demo – Search functionality.
Searches for "MacBook", verifies results page loads with relevant products.
URL: https://opencart.abstracta.us/
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://opencart.abstracta.us/"
SEARCH_TERM = "MacBook"


@pytest.mark.pass_test
def test_search_pass(driver):
    """
    1. Go to OpenCart demo homepage
    2. Type 'MacBook' in the search box
    3. Click the search button
    4. Verify the results page contains at least one relevant product
    """

    driver.get(BASE_URL)

    # ── Locate the search input field ─────────────────────────────────────────
    search_box = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )
    search_box.clear()
    search_box.send_keys(SEARCH_TERM)

    # ── Click the search button ───────────────────────────────────────────────
    search_btn = driver.find_element(By.CSS_SELECTOR, "button.btn-default[type='button']")
    search_btn.click()

    # ── Wait for results page ─────────────────────────────────────────────────
    WebDriverWait(driver, 15).until(EC.url_contains("search"))

    assert "search" in driver.current_url, (
        f"Expected search URL, got: {driver.current_url}"
    )

    # ── Check that search results container is present ────────────────────────
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".product-thumb, #product-list .product-layout")
        )
    )
    assert len(results) > 0, f"Expected at least 1 result for '{SEARCH_TERM}', found 0"

    # ── Verify at least one product name contains 'MacBook' ───────────────────
    product_names = [
        r.find_element(By.CSS_SELECTOR, ".caption h4 a, h4 a").text
        for r in results
        if r.find_elements(By.CSS_SELECTOR, ".caption h4 a, h4 a")
    ]
    assert any(SEARCH_TERM in name for name in product_names), (
        f"None of the results contain '{SEARCH_TERM}'. Found: {product_names}"
    )
