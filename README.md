# 🧪 Saucedemo QA Automation

Basic test automation project using **Selenium + Pytest** against [saucedemo.com](https://www.saucedemo.com).

---

## 📁 Project Structure

```
saucedemo_qa/
│
├── README.md
├── requirements.txt
├── __init__.py
│
└── tests/
    ├── login_page.py        # Page Object Model for the login screen
    ├── inventory_page.py    # Page Object Model for the products page
    ├── test_login.py        # Login test cases
    └── test_inventory.py    # Inventory test cases
```

---

## ⚙️ Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Running the tests

Run all tests:
```bash
pytest tests/
```

Run a specific file:
```bash
pytest tests/test_login.py
pytest tests/test_inventory.py
```

Run a single test:
```bash
pytest tests/test_login.py::TestLogin::test_successful_login
```

---

## 👤 Saucedemo test users

| Username | Password | Status |
|---|---|---|
| `standard_user` | `secret_sauce` | ✅ Normal |
| `locked_out_user` | `secret_sauce` | 🔒 Blocked |
| `problem_user` | `secret_sauce` | 🐛 Visual bugs |
| `performance_glitch_user` | `secret_sauce` | 🐌 Slow on purpose |
