"""
test_logout_pass.py
-------------------
PASS test: Logs in to SauceDemo, opens the burger menu, and logs out.
Verifies the user is redirected back to the login page.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


@pytest.mark.pass_test
def test_logout_pass(driver):
    """Full login → logout flow; asserts user lands back on the login page."""

    # ── Step 1: Login ──────────────────────────────────────────────────────────
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    # ── Step 2: Open the sidebar / burger menu ─────────────────────────────────
    driver.find_element(By.ID, "react-burger-menu-btn").click()

    # ── Step 3: Click the logout link ─────────────────────────────────────────
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_link.click()

    # ── Assertions ────────────────────────────────────────────────────────────
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "/"))

    login_btn = driver.find_element(By.ID, "login-button")
    assert login_btn.is_displayed(), "Login button must reappear after logout"
    assert driver.current_url.rstrip("/") == BASE_URL, (
        f"Expected login page URL, got: {driver.current_url}"
    )
