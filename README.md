# 🏦 Python Bank Management System

A **modular, PostgreSQL-backed terminal application** for managing bank operations. This project supports creating, updating, authenticating, saving, and deleting bank accounts, along with generating account statements and transaction histories — all securely handled in Python.

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

This project is a **terminal-driven Bank Management System** designed with modular architecture, secure PostgreSQL-based storage, and robust authentication. It’s ideal for learning database interaction, system design, and modular programming in Python.

---

## ✨ Features

- 🆕 Create New Bank Accounts with full details
- 📝 Update Account Information (Name, Email, Contact, Type, Password, UID)
- 🔐 Secure Password-Based Authentication
- 🔁 Deposit, Withdraw, and Transfer Funds
- 🔍 View Account Balance and Details
- 💾 PostgreSQL Database Integration for all operations
- 📑 Print and Save Bank Statements
- 🧾 View and Save Transaction Histories
- 🛡️ Admin Mode for full data access via Master Key
- 🗑️ Account Deletion (including DB cleanup)
- 🔄 Modular design with reusable utilities
- 🔒 Secure Encryption and Decryption for Password Handling

---

## 🧱 Folder Structure

```
Banking System/
├── accounts/                # (Deprecated) – Previously stored account files
├── bank statements/         # Stores printed statements
├── transaction history/     # Stores transaction logs
├── main.py                  # Entry point of the system
├── bank_menu.py             # Menu system with database support
├── account_ops.py           # Account creation/deletion/updates
├── bank_core.py             # Bank class and logic
├── transactions.py          # Credit/debit/transfer logic
├── utils.py                 # Utilities for email, UID, etc.
├── auth.py                  # Authentication and verification
├── load.py                  # Load logic (adapted to PostgreSQL)
├── constants.py             # Master key and DB config via dotenv
└── README.md
```

---

## 🧩 Modules Explained

| Module           | Description                                              |
|------------------|----------------------------------------------------------|
| `main.py`        | Entry point of the application                           |
| `bank_menu.py`   | Menu-driven routing of operations                        |
| `account_ops.py` | Create, delete, update accounts                          |
| `bank_core.py`   | `Bank` class with methods for transactions & updates     |
| `transactions.py`| Core logic for credit, debit, transfer                   |
| `utils.py`       | Account number generator, email validator, etc.          |
| `auth.py`        | Handles login, UID check, password validation            |
| `load.py`        | PostgreSQL-based data loading                            |
| `constants.py`   | Loads `MASTER_KEY` and DB config from `.env`             |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x installed
- PostgreSQL Server running
- `psycopg2` and `python-dotenv` installed:
  ```bash
  pip install psycopg2-binary python-dotenv
  ```

### 🛠️ Setup

1. Create a `.env` file in your root directory:

   ```env
   MASTER_KEY=your_secure_admin_password
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

2. Ensure your `Bank` table is created in PostgreSQL with appropriate columns (e.g., `acc_no`, `name`, `email`, `contact`, `type`, `password`, `uid`, `acc_balance`, etc.)

3. Run the app:

   ```bash
   python main.py
   ```

---

## 🎮 How to Use

- Navigate via terminal menu to:
  - Create, Update, or Delete accounts
  - Perform transactions and transfers
  - View or download account details
- Update features include:
  - Name, Email, Contact Number, Account Type, Password, and UID
- Admin (via master key) can:
  - View all accounts
  - Perform global database operations

---

## 🔐 Security

- Password-masked input using `getpass`
- Admin key stored securely via `.env`
- Max 3 login attempts per session
- Encrypted storage of passwords (basic encryption; upgrade recommended)
- UID validation to ensure uniqueness

---

## ⚠️ Known Limitations

- ❌ No GUI or web interface yet
- ❌ No password strength or reset mechanism
- ❌ Minimal error handling on DB failures
- ❌ No concurrent session or multi-user support

---

## 💡 Future Enhancements

- 🛢️ Add connection pooling and transaction rollback
- 🔐 Replace encryption with `bcrypt` for password hashing
- 🧪 Add unit and integration tests
- 🖥️ Flask or FastAPI web interface
- 📊 Admin dashboard with account analytics
- 📄 PDF exports for statements and logs

---

## 📜 License

MIT License — free to use, modify, and distribute.

---

## 👨‍💻 Author

**Adrishikhar Chowdhury**  
📧 amiadrishikhar@gmail.com  
🌐 [Portfolio Website](https://adrishikharchowdhury.glitch.me)
