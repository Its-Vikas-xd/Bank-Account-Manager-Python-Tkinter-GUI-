# 💰 Bank Account Manager - Tkinter GUI App

This is a **Python GUI application** built using the `tkinter` module. It simulates basic bank account operations such as creating an account, crediting and debiting money, and checking the balance — all through a simple and interactive interface.

---

## 🧰 Features

- ✅ Create a new account with account number and initial balance  
- 💳 Debit money from the account with balance validation  
- 💵 Credit money to the account  
- 📊 Check current account balance  
- 🖼️ Stylish and user-friendly interface with Tkinter  
- ❌ Error messages for invalid actions using messagebox dialogs

---

## 📁 Project Structure

### `Account` Class
Handles the core banking logic:
- `debit(amount)` – Deducts money from the balance if funds are sufficient
- `credit(amount)` – Adds money to the balance
- `get_balance()` – Returns the current balance

### `BankApp` Class (Tkinter GUI)
Creates and manages the graphical interface:
- Account setup form (account number and initial balance)
- Transaction panel with:
  - Amount entry field
  - Buttons for Debit, Credit, Balance check, and Exit
- Real-time messages and error handling

---

## 📦 Requirements

- Python 3.x  
- Tkinter (comes pre-installed with standard Python distributions)

---

## ▶️ How to Run

1. Save the code in a Python file, for example: `banking_System.py`  
2. Open a terminal or command prompt  
3. Run the app:

```bash
Banking_system.py
