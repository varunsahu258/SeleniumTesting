"""
test_iframe_fail.py
-------------------
FAIL test: Attempts to interact with iframe content WITHOUT switching context.
Selenium will NOT find the element inside the iframe → NoSuchElementException.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/iframe"


@pytest.mark.fail_test
def test_iframe_fail(driver):
    """
    INTENTIONAL FAILURE:
    Tries to find #tinymce without switching into the iframe first.
    Selenium cannot cross frame boundary — raises NoSuchElementException.
    """

    driver.get(BASE_URL)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "mce_0_ifr"))
    )

    # ── Missing: driver.switch_to.frame(...) ─────────────────────────────────
    # Directly access iframe-internal element from parent context — will fail
    editor_body = driver.find_element(By.ID, "tinymce")   # NoSuchElementException

    editor_body.send_keys("This line is never reached")
    assert editor_body.text == "This line is never reached"
