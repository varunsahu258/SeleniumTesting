"""
test_drag_drop_fail.py
----------------------
FAIL test: Asserts column headers swapped without actually performing the drag.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/drag_and_drop"


@pytest.mark.fail_test
def test_drag_drop_fail(driver):
    """
    INTENTIONAL FAILURE:
    Skips the drag action entirely and asserts that column-a header reads 'B'.
    The headers were never swapped — assertion fails.
    """

    driver.get(BASE_URL)

    col_a = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "column-a"))
    )

    # ── No drag performed ────────────────────────────────────────────────────
    header_text = col_a.find_element(By.TAG_NAME, "header").text

    # ── Wrong assertion: still reads 'A', not 'B' ─────────────────────────────
    assert header_text == "B", (
        f"[EXPECTED FAILURE] No drag was performed. "
        f"column-a still reads '{header_text}', not 'B'."
    )
