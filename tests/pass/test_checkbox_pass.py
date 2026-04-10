"""
test_checkbox_pass.py
---------------------
PASS test: Uses The Internet – Checkboxes page.
Checks and un-checks boxes, verifying state after each action.
URL: https://the-internet.herokuapp.com/checkboxes
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/checkboxes"


@pytest.mark.pass_test
def test_checkbox_pass(driver):
    """
    1. Verify initial checkbox states
    2. Toggle checkbox 1 to checked
    3. Toggle checkbox 2 to unchecked
    4. Assert final states
    """

    driver.get(BASE_URL)

    # ── Locate both checkboxes ────────────────────────────────────────────────
    checkboxes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")
        )
    )
    assert len(checkboxes) == 2, f"Expected 2 checkboxes, found {len(checkboxes)}"

    checkbox1, checkbox2 = checkboxes

    # ── Verify initial state (checkbox1=unchecked, checkbox2=checked) ─────────
    assert not checkbox1.is_selected(), "Checkbox 1 should start unchecked"
    assert checkbox2.is_selected(), "Checkbox 2 should start checked"

    # ── Toggle checkbox 1 → checked ───────────────────────────────────────────
    checkbox1.click()
    assert checkbox1.is_selected(), "Checkbox 1 should be checked after clicking"

    # ── Toggle checkbox 2 → unchecked ─────────────────────────────────────────
    checkbox2.click()
    assert not checkbox2.is_selected(), "Checkbox 2 should be unchecked after clicking"

    # ── Toggle checkbox 1 back → unchecked ───────────────────────────────────
    checkbox1.click()
    assert not checkbox1.is_selected(), "Checkbox 1 should be unchecked after second click"
