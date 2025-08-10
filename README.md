# 💳 Bank Account Management System (Python)

The **Bank Account Management System** is a Python-based console application that allows users to create and manage **Simple** and **Saving** bank accounts.
It provides essential banking operations like creating accounts, depositing and withdrawing money, viewing balances, applying interest (for savings accounts), and saving/loading account data from a file.

This project demonstrates **Object-Oriented Programming (OOP)** concepts such as **inheritance**, **method overriding**, and **encapsulation**, along with **file handling** for persistent storage.

---

## Features

* **Create Accounts**

  * Simple Account
  * Saving Account
* **Deposit Money** (with validation)
* **Withdraw Money** (with insufficient balance checks)
* **Show Balance**
* **Apply Interest** (for savings accounts)
* **View All Accounts** (simple & savings separately)
* **Persistent Data Storage** (save & load from file)
* **Error Handling** (prevents crashes on invalid input)

---

## 🛠 Technologies Used

* **Python 3.x**
* Object-Oriented Programming (OOP)
* File Handling (`.txt` file storage)
* Exception Handling

---

## 📂 Project Structure

```
BankAccountManagementSystem.py   # Main application file
accounts.txt                     # Data storage file (created automatically)
```

---

## How It Works

1. **Load Data**

   * When the program starts, it loads existing accounts from `accounts.txt` (if available).
2. **Main Menu**

   * Users choose from options like creating an account, depositing, withdrawing, etc.
3. **Account Types**

   * **Simple Account** → Basic deposit, withdraw, and balance check features.
   * **Saving Account** → Same as simple but can apply interest.
4. **Persistent Storage**

   * All account data is saved before exiting.
   * On the next run, accounts are restored from the file.

---

## Example Usage

**Main Menu:**

```
1. CREATE ACCOUNT
2. DEPOSIT MONEY
3. WITHDRAW MONEY
4. SHOW BALANCE
5. APPLY INTEREST
6. SEE ALL ACCOUNTS
7. SAVE & EXIT
```

**Sample Output:**

```
=======CREATE ACCOUNT=======
WRITE ACCOUNT NUMBER: 101
WRITE ACCOUNT HOLDER NAME: John Doe
STARTING BALANCE: 5000
Account for John Doe created successfully with balance 5000.0.
```

---

## Key Learning Points

* Using **OOP concepts** in Python for real-world applications.
* Implementing **file storage** for data persistence.
* Structuring programs for **scalability and readability**.
* Adding **error handling** to make programs user-friendly.

---

## Future Improvements

* Add **PIN-based authentication** for accounts.
* Implement **transaction history logs**.
* Use a **database (SQLite/MySQL)** instead of text files.
* Add **account deletion** feature.

---

## 👨‍💻 Author

**Ehtisham Aflaq** – Beginner Python Developer passionate about building real-world projects.

---
If you want, I can also make you a **well-formatted GitHub README with emojis, section dividers, and code formatting** so it looks attractive and professional when you upload your project.
Do you want me to prepare that stylish GitHub version for you?
