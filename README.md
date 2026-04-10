# 🧪 Selenium Test Suite — Python + Pytest

A production-quality automation suite covering 15 test scenarios,
each with a **PASS** and an **FAIL** variant (30 test scripts total).

---

## 📁 Folder Structure

```
selenium_suite/
├── conftest.py                        ← Shared WebDriver + Wait fixtures
├── pytest.ini                         ← Pytest configuration
├── requirements.txt                   ← Python dependencies
└── tests/
    ├── pass/
    │   ├── test_login_pass.py
    │   ├── test_invalid_login_pass.py
    │   ├── test_logout_pass.py
    │   ├── test_add_to_cart_pass.py
    │   ├── test_count_products_pass.py
    │   ├── test_navigation_pass.py
    │   ├── test_checkbox_pass.py
    │   ├── test_dropdown_pass.py
    │   ├── test_alert_pass.py
    │   ├── test_hover_pass.py
    │   ├── test_iframe_pass.py
    │   ├── test_drag_drop_pass.py
    │   ├── test_window_pass.py
    │   ├── test_scroll_pass.py
    │   └── test_search_pass.py
    └── fail/
        ├── test_login_fail.py
        ├── test_invalid_login_fail.py
        ├── test_logout_fail.py
        ├── test_add_to_cart_fail.py
        ├── test_count_products_fail.py
        ├── test_navigation_fail.py
        ├── test_checkbox_fail.py
        ├── test_dropdown_fail.py
        ├── test_alert_fail.py
        ├── test_hover_fail.py
        ├── test_iframe_fail.py
        ├── test_drag_drop_fail.py
        ├── test_window_fail.py
        ├── test_scroll_fail.py
        └── test_search_fail.py
```

---

## ⚙️ Test Websites Used

| Suite Area         | Website                                      |
|--------------------|----------------------------------------------|
| Login / Cart / Nav | https://www.saucedemo.com                    |
| Checkbox           | https://the-internet.herokuapp.com/checkboxes|
| Dropdown           | https://the-internet.herokuapp.com/dropdown  |
| Alert              | https://the-internet.herokuapp.com/javascript_alerts |
| Hover              | https://the-internet.herokuapp.com/hovers    |
| iFrame             | https://the-internet.herokuapp.com/iframe    |
| Drag & Drop        | https://the-internet.herokuapp.com/drag_and_drop |
| Multiple Windows   | https://the-internet.herokuapp.com/windows   |
| Scroll             | https://the-internet.herokuapp.com/infinite_scroll |
| Search             | https://opencart.abstracta.us/               |

---

## 🛠️ Installation

### 1. Prerequisites
- Python 3.9+
- Google Chrome (latest stable)
- ChromeDriver matching your Chrome version (or use `webdriver-manager`)

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Auto-manage ChromeDriver via webdriver-manager
If you prefer automatic ChromeDriver management, update `conftest.py`:
```python
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)
```

---

## 🚀 Running Tests

### Run ALL tests
```bash
pytest tests/ -v
```

### Run only PASS tests
```bash
pytest tests/pass/ -v
```

### Run only FAIL tests
```bash
pytest tests/fail/ -v
```

### Run a single test file
```bash
pytest tests/pass/test_login_pass.py -v
pytest tests/fail/test_login_fail.py -v
```

### Run by marker
```bash
pytest -m pass_test -v
pytest -m fail_test -v
```

### Run a specific test function by name
```bash
pytest -k "test_login" -v
pytest -k "test_alert_js_prompt_pass" -v
```

---

## 📊 HTML Reports

Generate a self-contained HTML report:
```bash
pytest tests/ -v --html=reports/report.html --self-contained-html
```

---

## ⚡ Parallel Execution (pytest-xdist)

Run tests in parallel across 4 CPU workers:
```bash
pytest tests/ -v -n 4
```

Run pass and fail suites in parallel:
```bash
pytest tests/pass/ -n auto -v
pytest tests/fail/ -n auto -v
```

> **Note:** Each test already uses `scope="function"` fixtures, so parallel
> execution is safe — each worker spins up its own WebDriver instance.

---

## 💡 Scaling Tips

| Goal                          | Tool / Approach                                      |
|-------------------------------|------------------------------------------------------|
| Parallel browser tests        | `pytest-xdist` with `-n auto`                        |
| Cross-browser testing         | Parameterize the `driver` fixture with Firefox/Edge  |
| Remote / cloud grid           | Switch to `webdriver.Remote` + Selenium Grid / BrowserStack |
| Retry flaky tests             | `pytest-rerunfailures` with `--reruns 2`             |
| Rich HTML report              | `pytest-html` — `--html=report.html`                 |
| Allure reports                | `pytest-allure` + Allure CLI                         |
| CI/CD integration             | Add `pytest tests/ --tb=short -q` to GitHub Actions / GitLab CI |
| Screenshot on failure         | Hook `pytest_runtest_makereport` in conftest.py      |
| Page Object Model             | Promote locators into `pages/` classes when suite grows |

---

## 🔍 Why FAIL Tests Fail

| Test File                    | Failure Reason                                         |
|------------------------------|--------------------------------------------------------|
| test_login_fail              | Wrong password → wrong URL assertion                   |
| test_invalid_login_fail      | Empty form shows error, but we assert error NOT shown  |
| test_logout_fail             | Clicks hidden element without opening sidebar menu     |
| test_add_to_cart_fail        | 1 item added, assert badge = "2"                       |
| test_count_products_fail     | 6 products exist, assert count = 10                    |
| test_navigation_fail         | Inventory URL, assert contains "checkout"              |
| test_checkbox_fail           | Box just checked, assert it is UNchecked               |
| test_dropdown_fail           | Option 1 selected, assert Option 2 is selected         |
| test_alert_fail              | Alert dismissed (Cancel), assert "Ok" in result        |
| test_hover_fail              | Caption queried without hovering → not visible         |
| test_iframe_fail             | tinymce queried without switching into iframe          |
| test_drag_drop_fail          | No drag performed, assert header swapped               |
| test_window_fail             | No window switch, assert new-window heading            |
| test_scroll_fail             | No scrolling, assert item count increased              |
| test_search_fail             | Garbage search term, assert results found              |
