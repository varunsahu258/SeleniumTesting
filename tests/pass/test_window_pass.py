"""
test_window_pass.py
-------------------
PASS test: The Internet – Multiple Windows page.
Opens a new window via the link, switches to it, verifies content,
then closes it and switches back to the original.
URL: https://the-internet.herokuapp.com/windows
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/windows"


@pytest.mark.pass_test
def test_window_pass(driver):
    """
    1. Open Multiple Windows page
    2. Click 'Click Here' → new window opens
    3. Switch to new window, verify its heading
    4. Close new window, switch back, verify original window
    """

    driver.get(BASE_URL)

    original_handle = driver.current_window_handle
    assert len(driver.window_handles) == 1, "Should start with exactly 1 window"

    # ── Click link that opens a new window ────────────────────────────────────
    driver.find_element(By.LINK_TEXT, "Click Here").click()

    # ── Wait until a second window handle appears ─────────────────────────────
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    all_handles = driver.window_handles
    assert len(all_handles) == 2, f"Expected 2 windows, got {len(all_handles)}"

    # ── Switch to the new window ──────────────────────────────────────────────
    new_handle = [h for h in all_handles if h != original_handle][0]
    driver.switch_to.window(new_handle)

    # ── Verify new window content ─────────────────────────────────────────────
    heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h3"))
    )
    assert heading.text == "New Window", (
        f"New window heading should be 'New Window', got '{heading.text}'"
    )
    assert "new_window" in driver.current_url, (
        f"Expected 'new_window' in URL, got: {driver.current_url}"
    )

    # ── Close new window and return to original ───────────────────────────────
    driver.close()
    driver.switch_to.window(original_handle)

    assert len(driver.window_handles) == 1, "Should have only 1 window after closing new one"
    assert "windows" in driver.current_url, (
        f"Should be back on original windows page. Got: {driver.current_url}"
    )
