
# 🏦 Python Bank Management System

A **modular, file-based terminal application** for managing bank operations. This project supports creating, updating, authenticating, saving, and deleting bank accounts, along with generating account statements and transaction histories — all securely handled in Python.

---

## 📚 Table of Contents

- [📌 Overview](#overview)
- [✨ Features](#features)
- [🧱 Folder Structure](#folder-structure)
- [🧩 Modules Explained](#modules-explained)
- [🚀 Getting Started](#getting-started)
- [🎮 How to Use](#how-to-use)
- [🔐 Security](#security)
- [⚠️ Known Limitations](#known-limitations)
- [💡 Future Enhancements](#future-enhancements)
- [📜 License](#license)
- [👨‍💻 Author](#author)

---

## 📌 Overview

This project is a **fully terminal-driven Bank Management System** designed with modular architecture, persistence through CSV, and secure operations. Ideal for learning file operations, user authentication, modular programming, and system design in Python.

---

## ✨ Features

- 🆕 Create New Bank Accounts with full details
- 🔐 Secure Password-Based Authentication
- 🔁 Deposit, Withdraw, and Transfer Funds
- 🔍 View Account Balance and Details
- 📂 Save, Load, and Delete Account Files
- 📑 Print and Save Bank Statements
- 🧾 View and Save Transaction Histories
- 🛡️ Admin Mode for full data access via Master Key
- 🗑️ Account Deletion (with file removal)
- 🔄 Modular design with reusable utilities
- 🔒 Secure Encryption and Decryption for Password Handling

---

## 🧱 Folder Structure
```
Banking System/
├── accounts/                # Stores saved account files
├── bank statements/         # Stores printed statements
├── transaction history/     # Stores transaction logs
├── main.py                  # Entry point of the system
├── bank_menu.py             # Main menu system
├── account_ops.py           # Create/delete accounts
├── bank_core.py             # Bank class and logic
├── transactions.py          # Credit/debit/transfer logic
├── utils.py                 # Utilities for email, UID, etc.
├── auth.py                  # Authentication and verification
├── load.py                  # File loading functions
├── constants.py             # Master key using dotenv
└── README.md
```

---

## 🧩 Modules Explained

| Module           | Description                                              |
|------------------|----------------------------------------------------------|
| `main.py`        | Entry point of the application                           |
| `bank_menu.py`   | Menu-driven routing of operations                        |
| `account_ops.py` | Account creation and deletion                            |
| `bank_core.py`   | `Bank` class with debit, credit, save, delete, print     |
| `transactions.py`| Core transaction logic (debit/credit)                    |
| `utils.py`       | Account number generation, email validation              |
| `auth.py`        | User and master key authentication                       |
| `load.py`        | Loading bank objects and transaction logs from file      |
| `constants.py`   | Loads `MASTER_KEY` from environment                      |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x installed
- `python-dotenv` if using `.env` file (optional)

### 🛠️ Run Instructions

1. Set a master key in your `.env` file:
   ```env
   MASTER_KEY=your_secure_admin_password
   ```

2. Run the program:
   ```bash
   python main.py
   ```

> 💡 You can also use a `run.bat` to execute from CMD on Windows.

---

## 🎮 How to Use

- Upon first run, create new accounts if no saved files exist.
- Navigate the menu to perform:
  - Account transactions
  - Fund transfers
  - Balance checks
  - Viewing/downloading details
  - Deleting accounts (with file removal)
- Admin-level access (via master key) is needed to:
  - View all accounts
  - Save/load all accounts
  - Delete accounts (which also deletes their associated files)

---

## 🔐 Security

- Password-protected user accounts
- Max 3 login attempts per session
- Admin control via a `.env` file storing `MASTER_KEY`
- No password is shown during typing (uses `getpass`)
- **Encryption** is used for storing passwords securely, using the master key

---

## ⚠️ Known Limitations

- ❌ No GUI or web interface
- ❌ File storage only — no database yet
- ❌ No password strength validation
- ❌ Not suitable for multi-user or concurrent environments

---

## 💡 Future Enhancements

- 📦 Switch to SQLite or JSON for better data management
- 🌐 Build a Flask-based web version
- 🔐 Add password hashing with `bcrypt`
- 🧾 PDF export of statements and receipts
- 📊 Dashboard for insights and visualizations
- 🧪 Add unit tests for reliability

---

## 📜 License

MIT License — feel free to use, modify, and distribute.

---

## 👨‍💻 Author

**Adrishikhar Chowdhury**  
📧 amiadrishikhar@gmail.com  
🌐 [Portfolio Website](https://adrishikharchowdhury.glitch.me)