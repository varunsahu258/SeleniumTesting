"""
test_hover_fail.py
------------------
FAIL test: Asserts hover caption is visible WITHOUT performing the hover.
The caption is hidden by default — assertion will fail.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/hovers"


@pytest.mark.fail_test
def test_hover_fail(driver):
    """
    INTENTIONAL FAILURE:
    Skips hover action entirely and asserts the hidden caption is visible.
    The caption only appears on hover — assertion will fail.
    """

    driver.get(BASE_URL)

    figures = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".figure"))
    )

    # ── No hover performed — caption is still hidden ───────────────────────────
    caption = figures[0].find_element(By.CSS_SELECTOR, ".figcaption")

    # ── Wrong assertion: caption is NOT visible without hover ──────────────────
    assert caption.is_displayed(), (
        "[EXPECTED FAILURE] Caption should NOT be visible without hovering. "
        "We skipped the hover action intentionally."
    )
