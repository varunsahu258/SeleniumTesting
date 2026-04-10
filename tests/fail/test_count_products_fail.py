"""
test_count_products_fail.py
---------------------------
FAIL test: Asserts product count equals 10 — SauceDemo only has 6.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.fail_test
def test_count_products_fail(driver):
    """
    INTENTIONAL FAILURE:
    SauceDemo has 6 products but we assert 10 — test must fail.
    """

    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item"))
    )

    products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")

    # ── Wrong count assertion ─────────────────────────────────────────────────
    assert len(products) == 10, (
        f"[EXPECTED FAILURE] Expected 10 products but found {len(products)}"
    )
