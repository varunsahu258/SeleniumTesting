"""
test_iframe_pass.py
-------------------
PASS test: The Internet – iFrame page (TinyMCE editor).
Switches into the iframe, clears content, types new text,
then switches back and verifies page structure.
URL: https://the-internet.herokuapp.com/iframe
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/iframe"


@pytest.mark.pass_test
def test_iframe_pass(driver):
    """
    1. Navigate to iframe page
    2. Switch into the TinyMCE iframe
    3. Clear existing text, type new content
    4. Switch back to default content
    5. Verify toolbar is still visible
    """

    driver.get(BASE_URL)

    # ── Wait for the iframe to be present ─────────────────────────────────────
    iframe = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "mce_0_ifr"))
    )

    # ── Switch into the iframe ────────────────────────────────────────────────
    driver.switch_to.frame(iframe)

    # ── Locate the editable body inside iframe ────────────────────────────────
    editor_body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "tinymce"))
    )

    # ── Clear and type new content ────────────────────────────────────────────
    editor_body.clear()
    editor_body.click()
    editor_body.send_keys("Selenium iframe test content")

    typed_text = editor_body.text
    assert "Selenium iframe test content" in typed_text, (
        f"Text not typed correctly inside iframe. Got: '{typed_text}'"
    )

    # ── Switch back to the main document ──────────────────────────────────────
    driver.switch_to.default_content()

    # ── Verify the toolbar still exists outside the iframe ────────────────────
    toolbar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".tox-toolbar__primary, "
                                                           ".mce-toolbar, #mce-external-root"))
    )
    # Page heading must be present
    heading = driver.find_element(By.CSS_SELECTOR, "h3")
    assert heading.is_displayed(), "Page heading not visible after switching out of iframe"
    assert "An iFrame" in heading.text, f"Unexpected heading: {heading.text}"
