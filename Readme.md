# SauceDemo Playwright Automation Project

This project contains automated UI tests for the SauceDemo website using Python, Playwright, and Pytest. It covers login validation, product sorting, adding items to the cart, and checkout flow.

## Project Overview

- Website under test: https://www.saucedemo.com/
- Automation tool: Playwright
- Test framework: Pytest
- Page object model: implemented using Python classes in the `pages` folder
- Shared browser/page setup: defined in `conftest.py`

## Tech Stack

- Python 3.10+
- Pytest
- Playwright
- VS Code (recommended)

## Repository Structure

```text
PP1/
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
└── venv/
```

## Prerequisites

Before running the tests, make sure the following are installed on your machine:

1. Git
2. Python 3.10 or newer
3. A modern browser (Chrome/Chromium is used by default in this project)

## Clone the Project

```bash
git clone <your-repository-url>
cd PP1
```

## Set Up a Virtual Environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

Install the required Python packages:

```bash
pip install pytest playwright
```

Then install the browser binaries for Playwright:

```bash
python -m playwright install
```

If your system requires additional browser dependencies, use:

```bash
python -m playwright install --with-deps
```

## Run the Tests

From the project root, run:

```bash
pytest -q
```

To run a specific test file:

```bash
pytest tests/test_saucedemoLogin.py -q
```

To run a single test:

```bash
pytest tests/test_inventory.py -k "checkout" -q
```

