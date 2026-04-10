"""
test_hover_pass.py
------------------
PASS test: The Internet – Hovers page.
Hovers over each user card and verifies the hidden caption appears.
URL: https://the-internet.herokuapp.com/hovers
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

BASE_URL = "https://the-internet.herokuapp.com/hovers"


@pytest.mark.pass_test
def test_hover_pass(driver):
    """
    Hover over each of the 3 user figure cards.
    After each hover the caption div must become visible and
    contain the expected username text.
    """

    driver.get(BASE_URL)

    # ── Wait for all figure cards to load ─────────────────────────────────────
    figures = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".figure"))
    )
    assert len(figures) == 3, f"Expected 3 hover cards, found {len(figures)}"

    actions = ActionChains(driver)

    for idx, figure in enumerate(figures, start=1):
        # ── Perform hover ──────────────────────────────────────────────────────
        actions.move_to_element(figure).perform()

        # ── Wait for caption to become visible ────────────────────────────────
        caption = WebDriverWait(driver, 10).until(
            EC.visibility_of(figure.find_element(By.CSS_SELECTOR, ".figcaption"))
        )

        assert caption.is_displayed(), f"Caption for figure {idx} should be visible on hover"

        # Caption must contain "user" text (e.g. "name: user1")
        caption_text = caption.text.lower()
        assert "user" in caption_text, (
            f"Caption {idx} missing 'user' text: '{caption_text}'"
        )

        # "View profile" link must be present inside caption
        profile_link = figure.find_element(By.CSS_SELECTOR, ".figcaption a")
        assert profile_link.is_displayed(), f"Profile link not visible for figure {idx}"
        assert "/users/" in profile_link.get_attribute("href"), (
            f"Unexpected href for figure {idx}: {profile_link.get_attribute('href')}"
        )
