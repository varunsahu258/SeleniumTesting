"""
test_drag_drop_pass.py
----------------------
PASS test: The Internet – Drag and Drop page.
Drags column A onto column B and verifies the swap via JS-based drag helper.
URL: https://the-internet.herokuapp.com/drag_and_drop
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

BASE_URL = "https://the-internet.herokuapp.com/drag_and_drop"

# JS helper that simulates an HTML5 drag-and-drop event (native DnD API bypass)
DND_JS = """
function simulateDnD(src, tgt) {
    function createDTWithData() {
        const dt = { data: {}, setData: (k,v)=>dt.data[k]=v,
                     getData: k=>dt.data[k], types: [],
                     effectAllowed: 'all', dropEffect: 'move' };
        return dt;
    }
    const dt = createDTWithData();
    function fire(el, type, extras) {
        const ev = new DragEvent(type, Object.assign({bubbles:true,cancelable:true}, extras));
        Object.defineProperty(ev, 'dataTransfer', {value: dt});
        el.dispatchEvent(ev);
    }
    fire(src, 'dragstart', {});
    fire(tgt, 'dragover', {});
    fire(tgt, 'drop', {});
    fire(src, 'dragend', {});
}
simulateDnD(arguments[0], arguments[1]);
"""


@pytest.mark.pass_test
def test_drag_drop_pass(driver):
    """
    Drag column A on top of column B.
    After the operation the headers should be swapped:
    column A header → 'B', column B header → 'A'.
    """

    driver.get(BASE_URL)

    col_a = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "column-a"))
    )
    col_b = driver.find_element(By.ID, "column-b")

    # ── Verify initial labels ─────────────────────────────────────────────────
    assert col_a.find_element(By.TAG_NAME, "header").text == "A", "Column A should start labeled 'A'"
    assert col_b.find_element(By.TAG_NAME, "header").text == "B", "Column B should start labeled 'B'"

    # ── Perform drag using JS helper (HTML5 DnD not natively supported by WebDriver) ──
    driver.execute_script(DND_JS, col_a, col_b)

    # ── Verify the swap ───────────────────────────────────────────────────────
    new_col_a_text = driver.find_element(By.ID, "column-a").find_element(By.TAG_NAME, "header").text
    new_col_b_text = driver.find_element(By.ID, "column-b").find_element(By.TAG_NAME, "header").text

    assert new_col_a_text == "B", f"After drag, column-a header should be 'B', got '{new_col_a_text}'"
    assert new_col_b_text == "A", f"After drag, column-b header should be 'A', got '{new_col_b_text}'"
