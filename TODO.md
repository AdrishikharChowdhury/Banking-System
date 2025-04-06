# 🏦 TODO.md — Banking System Project

Welcome to the development plan for the **Banking System** project. This document outlines everything you need to build a complete, well-structured banking application.

---

## 📌 Project Objective

Build a command-line or GUI-based banking system that allows users to register, log in, and manage their bank accounts (deposit, withdraw, check balance, transaction history). This system should be secure, modular, and extensible.

---

## 🧱 1. Project Structure

- [ ] Create a clean file structure:
  - `main.py` – entry point
  - `auth.py` – registration/login logic
  - `bank.py` – banking operations
  - `db.py` – data handling (read/write)
  - `utils.py` – utility functions (validation, formatting)
  - `models/` – account and user classes
  - `data/` – for persistent storage (JSON, CSV, DB)
  - `logs/` – log user activity/errors

---

## 🧩 2. Core Features

### 🧍 User Management
- [ ] User registration
  - [ ] Unique usernames
  - [ ] Secure password creation
- [ ] User login with verification
- [ ] Password hashing (use `hashlib` or `bcrypt`)
- [ ] Account locking after multiple failed login attempts

### 💰 Banking Operations
- [ ] Deposit
- [ ] Withdraw with balance check
- [ ] Balance inquiry
- [ ] Mini statement (last 5–10 transactions)
- [ ] Full transaction history
- [ ] Transfer between users (optional)

### 📁 Account Management
- [ ] Auto-generate unique account numbers
- [ ] Support for multiple accounts per user (e.g., savings, checking)
- [ ] View account info (type, creation date, etc.)

---

## 🧑‍💼 3. Admin Panel (Optional but Recommended)
- [ ] Admin login (separate from user accounts)
- [ ] View all users and balances
- [ ] View total bank balance
- [ ] Reset passwords or unlock user accounts
- [ ] Export all transaction logs

---

## 🧠 4. Data Persistence

Choose and implement at least one:

### 🔹 Option 1: File-based
- [ ] Use JSON or CSV files
  - [ ] Store user data
  - [ ] Store transactions per account
- [ ] Implement safe read/write operations

### 🔹 Option 2: Database
- [ ] SQLite integration (recommended)
  - [ ] Users table
  - [ ] Accounts table
  - [ ] Transactions table
- [ ] Use parameterized queries (prevent SQL injection)
- [ ] Modular DB functions

---

## 🧰 5. Utilities

- [ ] Input validation (e.g., amount must be > 0)
- [ ] Password strength check
- [ ] Date and time formatting (transaction timestamps)
- [ ] Number formatting (commas, currency symbol)
- [ ] Logging system (track logins, failed attempts, errors)

---

## 🎨 6. Interface (CLI first, then GUI optional)

### CLI (Command Line Interface)
- [ ] Menu-based navigation
- [ ] Clear prompts and messages
- [ ] Color output (optional, using `colorama`)

### GUI (Optional Enhancements)
- [ ] Tkinter-based desktop app
- [ ] Screens for login, dashboard, transaction pages

---

## 🧪 7. Testing

- [ ] Manual test cases for each feature
- [ ] Automated unit tests using `unittest` or `pytest`
  - [ ] Registration/login tests
  - [ ] Deposit/withdrawal tests
  - [ ] Data saving and reading
- [ ] Mock user inputs for testing flows

---

## 🛡️ 8. Security

- [ ] Encrypt passwords before storing
- [ ] Input sanitization to prevent code injection
- [ ] Mask password during typing (`getpass`)
- [ ] Lockout mechanism after multiple failed logins
- [ ] Admin-only access for sensitive features

---

## 📈 9. Advanced Features (Stretch Goals)

- [ ] Multi-currency support
- [ ] Interest calculation for savings accounts
- [ ] Email/SMS notification system (mocked)
- [ ] Account statement PDF export
- [ ] API version using Flask or FastAPI
- [ ] Dockerize the app for deployment
- [ ] Mobile app (React Native or Kivy)

---

## 🧹 10. Code Quality & Dev Practices

- [ ] Follow PEP8 standards
- [ ] Add comments and docstrings
- [ ] Use type hints (`def deposit(amount: float) -> bool:`)
- [ ] Refactor large functions into smaller units
- [ ] Add `README.md` with instructions
- [ ] Add `requirements.txt`
- [ ] Version control with Git
  - [ ] Create `.gitignore`
  - [ ] Use feature branches

---

## 📊 11. Documentation

- [ ] Full `README.md` with:
  - [ ] Project description
  - [ ] Setup instructions
  - [ ] Features list
  - [ ] Sample run (screenshots or output)
- [ ] Add inline code comments
- [ ] Flowcharts/diagrams (optional but useful)
- [ ] User manual PDF (if sharing with non-devs)

---

## ✅ Final Touches

- [ ] Perform full walkthrough as a user
- [ ] Test edge cases (e.g., withdrawing more than balance)
- [ ] Backup important data
- [ ] Make a final presentation/demo version

