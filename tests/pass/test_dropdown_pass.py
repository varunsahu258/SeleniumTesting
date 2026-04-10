"""
test_dropdown_pass.py
---------------------
PASS test: The Internet – Dropdown page.
Selects each option and verifies selection state.
URL: https://the-internet.herokuapp.com/dropdown
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

BASE_URL = "https://the-internet.herokuapp.com/dropdown"


@pytest.mark.pass_test
def test_dropdown_pass(driver):
    """
    Selects Option 1 and Option 2 in turn and verifies the selected value.
    """

    driver.get(BASE_URL)

    # ── Wait for the dropdown to be present ───────────────────────────────────
    dropdown_el = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dropdown"))
    )
    dropdown = Select(dropdown_el)

    # ── Check all available options ───────────────────────────────────────────
    options = [opt.text for opt in dropdown.options]
    assert "Option 1" in options, f"'Option 1' not found in dropdown: {options}"
    assert "Option 2" in options, f"'Option 2' not found in dropdown: {options}"

    # ── Select Option 1 ───────────────────────────────────────────────────────
    dropdown.select_by_visible_text("Option 1")
    assert dropdown.first_selected_option.text == "Option 1", (
        f"Expected 'Option 1', got '{dropdown.first_selected_option.text}'"
    )

    # ── Select Option 2 ───────────────────────────────────────────────────────
    dropdown.select_by_visible_text("Option 2")
    assert dropdown.first_selected_option.text == "Option 2", (
        f"Expected 'Option 2', got '{dropdown.first_selected_option.text}'"
    )

    # ── Select by value ───────────────────────────────────────────────────────
    dropdown.select_by_value("1")
    assert dropdown.first_selected_option.get_attribute("value") == "1", (
        "Selecting by value '1' did not work"
    )
