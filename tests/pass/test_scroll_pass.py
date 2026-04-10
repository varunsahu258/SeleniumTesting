"""
test_scroll_pass.py
-------------------
PASS test: The Internet – Infinite Scroll page (or fallback to Large Page).
Scrolls to the bottom of the page, verifies new content loaded,
then scrolls back to the top.
URL: https://the-internet.herokuapp.com/infinite_scroll
"""

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

BASE_URL = "https://the-internet.herokuapp.com/infinite_scroll"


@pytest.mark.pass_test
def test_scroll_pass(driver):
    """
    1. Load infinite scroll page
    2. Record initial paragraph count
    3. Scroll down several times
    4. Verify new paragraphs have been appended
    5. Scroll back to top and verify first paragraph still present
    """

    driver.get(BASE_URL)

    # ── Wait for at least one paragraph ───────────────────────────────────────
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".jscroll-added, div.infinite-scroll-component p, .entry"))
    )

    # Record initial item count
    initial_items = driver.find_elements(By.CSS_SELECTOR, ".jscroll-added, .entry")
    initial_count = len(initial_items)

    # ── Scroll down 4 times using JavaScript ─────────────────────────────────
    for _ in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)  # Brief pause to allow content to load after scroll

    # ── Verify more items loaded ───────────────────────────────────────────────
    all_items = driver.find_elements(By.CSS_SELECTOR, ".jscroll-added, .entry")
    assert len(all_items) > initial_count, (
        f"Expected more items after scrolling. "
        f"Before: {initial_count}, After: {len(all_items)}"
    )

    # ── Scroll back to top ────────────────────────────────────────────────────
    driver.execute_script("window.scrollTo(0, 0);")

    # Verify page heading is visible after scroll to top
    heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h3"))
    )
    assert heading.is_displayed(), "Page heading should be visible after scrolling to top"
    assert "Infinite Scroll" in heading.text, f"Unexpected heading: {heading.text}"
