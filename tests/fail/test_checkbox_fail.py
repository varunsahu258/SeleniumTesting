"""
test_checkbox_fail.py
---------------------
FAIL test: Checks checkbox 1 but wrongly asserts it is still unchecked.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/checkboxes"


@pytest.mark.fail_test
def test_checkbox_fail(driver):
    """
    INTENTIONAL FAILURE:
    Clicks checkbox 1 (making it checked) then asserts it is NOT selected.
    """

    driver.get(BASE_URL)

    checkboxes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")
        )
    )

    checkbox1 = checkboxes[0]

    # ── Click checkbox 1 to check it ──────────────────────────────────────────
    checkbox1.click()

    # ── Wrong assertion: checkbox is now checked, but we assert it isn't ──────
    assert not checkbox1.is_selected(), (
        "[EXPECTED FAILURE] Checkbox 1 WAS just checked but we assert it is unchecked."
    )
