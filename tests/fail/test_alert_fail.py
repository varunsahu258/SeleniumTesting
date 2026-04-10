"""
test_alert_fail.py
------------------
FAIL test: Dismisses a JS Confirm but wrongly asserts the result contains "Ok".
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/javascript_alerts"


@pytest.mark.fail_test
def test_alert_fail(driver):
    """
    INTENTIONAL FAILURE:
    Dismisses (Cancel) JS Confirm — result will say "Cancel".
    We then assert "Ok" is in the result — which is false.
    """

    driver.get(BASE_URL)

    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

    # ── Dismiss the alert (Cancel) ────────────────────────────────────────────
    alert.dismiss()

    result = driver.find_element(By.ID, "result")

    # ── Wrong assertion: after dismiss the text says "Cancel", not "Ok" ───────
    assert "Ok" in result.text, (
        f"[EXPECTED FAILURE] Alert was dismissed but we assert 'Ok'. "
        f"Actual result: '{result.text}'"
    )
