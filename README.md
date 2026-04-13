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
    ├── add_to_cart_test.py         # add items to cart and check the value
    ├── badge_change_test.py        # check that badge disappears when deleting item from cart
    ├── empty_login_test.py         # login with empty username field
    ├── empty_password_test.py      # login with empty password field
    ├── inventory_quantity_test.py  # test inventory items displayed on page
    ├── locked_user_test.py         # login with locked user
    ├── login_failed_test.py        # login with wrong credentials
    ├── login_test.py               # normal login
    ├── sort_items_test.py          # sort items by A-Z and by Z-A
    │
    └── workflows/
        ├── __init__.py
        ├── checkout_multiple_items.py   #Tests if multiple items are added to checkout      
        ├── complete_workflow_test.py    #test complete workflow, from login until checkout
        ├── empty_checkout_data_test.py  #tests if empty checkout data cannot be empty 
        └── sum_items_test.py            #tests if products sum in checkout are calculated correctly
   
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
