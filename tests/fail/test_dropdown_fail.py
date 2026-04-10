"""
test_dropdown_fail.py
---------------------
FAIL test: Selects Option 1, then wrongly asserts Option 2 is selected.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

BASE_URL = "https://the-internet.herokuapp.com/dropdown"


@pytest.mark.fail_test
def test_dropdown_fail(driver):
    """
    INTENTIONAL FAILURE:
    Selects 'Option 1' but then asserts 'Option 2' is the selected text.
    """

    driver.get(BASE_URL)

    dropdown_el = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dropdown"))
    )
    dropdown = Select(dropdown_el)

    # ── Select Option 1 ───────────────────────────────────────────────────────
    dropdown.select_by_visible_text("Option 1")

    # ── Wrong assertion ───────────────────────────────────────────────────────
    assert dropdown.first_selected_option.text == "Option 2", (
        f"[EXPECTED FAILURE] Selected 'Option 1' but asserted 'Option 2'. "
        f"Actual: '{dropdown.first_selected_option.text}'"
    )
