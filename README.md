
# 🏦 Bank Management System in Python

A **modular, terminal-based Bank Management System** built using Python. It simulates real-world banking operations such as account creation, authentication, transactions (credit/debit), and fund transfers — all while demonstrating clean software design principles and user interaction.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Modules Explained](#modules-explained)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Security](#security)
- [Known Limitations](#known-limitations)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 📌 Overview

This project is a **console-based banking system** created for educational purposes, personal experimentation, and as a showcase of Python programming with modular design.

No external dependencies or frameworks are used — everything is written in core Python with a focus on logic, modularity, and basic validation.

---

## ✨ Features

- ✅ **Create New Bank Accounts**
- 🔐 **Secure Authentication** with password and master key
- 💰 **Credit/Debit Transactions** with input validation
- 🔍 **Balance Enquiry**
- 🔁 **Transfer Funds** between accounts
- 📄 **View All Accounts** (protected by Master Key)
- 👤 **View Specific Account Details**
- 🧩 **Modular Design** for easy maintenance and scalability

---

## 🏗️ System Architecture

This system is **modular**, meaning it separates concerns across multiple files:

```
banking-system/
├── main.py               # Program entry point
├── bank_menu.py          # Interactive menu system
├── account_ops.py        # Account creation and user authentication
├── transactions.py       # Handles credit and debit operations
├── bank_core.py          # Bank class definition (business logic)
├── constants.py          # Global data and configurations
└── README.md             # Project documentation
```

---

## 📦 Modules Explained

| Module         | Purpose |
|----------------|---------|
| `main.py`      | Runs the banking system, handles flow control |
| `bank_menu.py` | Menu interface with all banking operations |
| `account_ops.py` | Contains `create_accounts` and `authenticator` functions |
| `transactions.py` | Manages `debit_balance` and `credit_balance` logic |
| `bank_core.py` | Defines the `Bank` class with methods like `credit`, `debit`, etc. |
| `constants.py` | Stores shared data and sensitive values like `__master_key` |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x installed
- Terminal or Command Prompt

### 🛠️ Installation

1. Clone or download the project:

```bash
git clone https://github.com/yourusername/python-banking-system.git
cd python-banking-system
```

2. Run the program:

```bash
python main.py
```

---

## 🎮 How to Use

1. On start, enter the number of accounts you want to create initially.
2. Provide name, account number, password, and opening balance.
3. Use the menu options to:
   - Debit or credit money
   - Transfer funds
   - View balance
   - View all accounts (with master key)
4. Each operation may require password authentication for security.

> ✅ Tip: Keep the account number and password handy. You’ll need them for authentication.

---

## 🔐 Security

- Each account is password-protected.
- 3 chances are given for password attempts.
- A **Master Key** allows admin-level access to view all accounts.
- By default, master key is:

```python
__master_key = "khul ja sim sim"
```

> Change it in `constants.py` for added security.

---

## ⚠️ Known Limitations

- ❌ No persistent storage — data is stored in-memory only (cleared on restart).
- ❌ No GUI — runs purely in a terminal window.
- ❌ No concurrency or multi-user support.
- ❌ No input validation for account name or password complexity.

---

## 💡 Future Enhancements

- 💾 Add file-based or database persistence (JSON/SQLite)
- 🌐 Add a web-based front end (Flask or Django)
- 🧪 Add unit tests for each module
- 🛡️ Add password hashing and encryption
- 📊 Export transaction history to files

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 👨‍💻 Author

**[Adrishikhar Chowhdury]**  
Python Developer & Tech Enthusiast  
📧 amiadrishikhar@gmail.com 
🌐 [portfolio](adrishikharchowdhury.glitch.me)

---

> “Code like you mean it. Debug like a detective. And document like a poet.” 💬
```