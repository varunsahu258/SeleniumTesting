"""
test_alert_pass.py
------------------
PASS test: The Internet – JavaScript Alerts page.
Tests JS Alert (accept), JS Confirm (dismiss & accept), JS Prompt (send keys).
URL: https://the-internet.herokuapp.com/javascript_alerts
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/javascript_alerts"


@pytest.mark.pass_test
def test_alert_js_alert_pass(driver):
    """Click 'JS Alert' button, accept it, verify result text."""

    driver.get(BASE_URL)

    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

    # ── Switch to alert and accept ────────────────────────────────────────────
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert alert.text == "I am a JS Alert", f"Unexpected alert text: {alert.text}"
    alert.accept()

    # ── Verify result message ─────────────────────────────────────────────────
    result = driver.find_element(By.ID, "result")
    assert result.text == "You successfully clicked an alert", (
        f"Unexpected result: {result.text}"
    )


@pytest.mark.pass_test
def test_alert_js_confirm_accept_pass(driver):
    """Click 'JS Confirm', accept it, verify 'Ok' result."""

    driver.get(BASE_URL)

    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()

    result = driver.find_element(By.ID, "result")
    assert "Ok" in result.text, f"Unexpected confirm result: {result.text}"


@pytest.mark.pass_test
def test_alert_js_prompt_pass(driver):
    """Click 'JS Prompt', type text, accept, verify text appears in result."""

    driver.get(BASE_URL)

    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.send_keys("Selenium QA")
    alert.accept()

    result = driver.find_element(By.ID, "result")
    assert "Selenium QA" in result.text, (
        f"Prompt input not reflected in result: {result.text}"
    )
