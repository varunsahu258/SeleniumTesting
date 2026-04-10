"""
test_scroll_fail.py
-------------------
FAIL test: Asserts new items loaded after scroll, but scroll is never triggered.
Count stays the same — assertion fails.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/infinite_scroll"


@pytest.mark.fail_test
def test_scroll_fail(driver):
    """
    INTENTIONAL FAILURE:
    Reads initial item count, skips scrolling, then asserts count increased.
    Without scrolling, no new content loads — assertion fails.
    """

    driver.get(BASE_URL)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".jscroll-added, .entry")
        )
    )

    initial_items = driver.find_elements(By.CSS_SELECTOR, ".jscroll-added, .entry")
    initial_count = len(initial_items)

    # ── No scrolling performed ────────────────────────────────────────────────

    after_items = driver.find_elements(By.CSS_SELECTOR, ".jscroll-added, .entry")

    # ── Wrong assertion: count hasn't changed without scrolling ───────────────
    assert len(after_items) > initial_count, (
        f"[EXPECTED FAILURE] No scrolling was done. "
        f"Count stayed at {len(after_items)}, expected > {initial_count}."
    )
