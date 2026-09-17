# SauceDemo — Playwright + Pytest (Python)

Automated UI tests for https://www.saucedemo.com/ using Python, Playwright, and Pytest.

Overview
- Tests cover login, product listing/sorting, add-to-cart, and basic checkout flows.
- Page objects live in the `pages/` folder; shared fixtures are in `conftest.py`.

Quick Start
1. Clone the repo and open the project root.

```bash
git clone https://github.com/UshaChapagain/Playwright.git
cd Saucedemo
```

2. Create and activate a virtual environment (Windows):

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install Python deps and Playwright browsers:

```bash
pip install -r requirements.txt
python -m playwright install
```

Project layout

```text
Saucedemo/
├── conftest.py
├── pytest.ini
├── Readme.md
├── pages/
│   ├── Inventorypage.py
│   └── page_saucedemoLogin.py
├── tests/
│   ├── test_inventory.py
│   ├── test_record.py
│   └── test_saucedemoLogin.py
├── assets/
│   └── style.css
├── allure-result/
└── requirements.txt
```

Running tests
- Run the entire suite:

```bash
pytest -v
```

- Run a single test file:

```bash
pytest tests/test_saucedemoLogin.py -q
```

- Run tests by keyword:

```bash
pytest -k "checkout" -q
```

Allure reports
- Collect results with pytest and the Allure plugin:

```bash
pip install allure-pytest
pytest --alluredir=allure-result
```

- Serve the results (requires `allure` CLI installed):

```bash
allure serve allure-result
```



