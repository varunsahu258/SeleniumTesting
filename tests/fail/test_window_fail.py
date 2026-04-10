"""
test_window_fail.py
-------------------
FAIL test: Opens a new window but never switches to it.
Asserts the heading of the new window while still on the original — fails.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/windows"


@pytest.mark.fail_test
def test_window_fail(driver):
    """
    INTENTIONAL FAILURE:
    A new window opens but we remain on the original.
    Asserting the new window's heading ('New Window') against the original
    page heading ('Opening a new window') — will fail.
    """

    driver.get(BASE_URL)

    driver.find_element(By.LINK_TEXT, "Click Here").click()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # ── Missing: driver.switch_to.window(new_handle) ───────────────────────────
    # We are still on the original window

    heading = driver.find_element(By.TAG_NAME, "h3")

    # ── Wrong assertion: original window heading is not 'New Window' ───────────
    assert heading.text == "New Window", (
        f"[EXPECTED FAILURE] Still on original window. "
        f"Heading is '{heading.text}', not 'New Window'."
    )
