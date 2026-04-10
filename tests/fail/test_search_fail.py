"""
test_search_fail.py
-------------------
FAIL test: Searches for a nonsense term and asserts results are found.
OpenCart returns no results for garbage input — assertion fails.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://opencart.abstracta.us/"
GARBAGE_TERM = "xyzzy_nonexistent_12345"


@pytest.mark.fail_test
def test_search_fail(driver):
    """
    INTENTIONAL FAILURE:
    Searches for a term that returns 0 results, then asserts results exist.
    """

    driver.get(BASE_URL)

    search_box = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )
    search_box.clear()
    search_box.send_keys(GARBAGE_TERM)

    search_btn = driver.find_element(By.CSS_SELECTOR, "button.btn-default[type='button']")
    search_btn.click()

    WebDriverWait(driver, 15).until(EC.url_contains("search"))

    results = driver.find_elements(
        By.CSS_SELECTOR, ".product-thumb, #product-list .product-layout"
    )

    # ── Wrong assertion: expects results for a nonexistent product ────────────
    assert len(results) > 0, (
        f"[EXPECTED FAILURE] Search for '{GARBAGE_TERM}' returned "
        f"{len(results)} results — expected > 0."
    )
