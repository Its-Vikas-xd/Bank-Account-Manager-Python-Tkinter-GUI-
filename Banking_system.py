import tkinter as tk
from tkinter import messagebox

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        if amount > self.balance:
            return (False, "Insufficient balance! Transaction failed.")
        self.balance -= amount
        return (True, f"₹{amount:.2f} debited\nNew balance: ₹{self.balance:.2f}")

    def credit(self, amount):
        self.balance += amount
        return (True, f"₹{amount:.2f} credited\nNew balance: ₹{self.balance:.2f}")

    def get_balance(self):
        return self.balance

class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bank Account Manager")
        self.geometry("500x500")
        self.configure(bg="#2C3E50")
        self.account = None

        # Setup Frame
        self.setup_frame = tk.Frame(self, bg="#2C3E50")
        self.setup_frame.pack(pady=40)

        tk.Label(self.setup_frame, text="Create New Account", font=("Arial", 16, "bold"), 
                bg="#2C3E50", fg="#ECF0F1").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.setup_frame, text="Account Number:", font=("Arial", 12), 
                bg="#2C3E50", fg="#BDC3C7").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.acc_entry = tk.Entry(self.setup_frame, font=("Arial", 12))
        self.acc_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.setup_frame, text="Initial Balance:", font=("Arial", 12), 
                bg="#2C3E50", fg="#BDC3C7").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.bal_entry = tk.Entry(self.setup_frame, font=("Arial", 12))
        self.bal_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.setup_frame, text="Create Account", command=self.create_account,
                 font=("Arial", 12, "bold"), bg="#27AE60", fg="white", relief="flat",
                 padx=20).grid(row=3, column=0, columnspan=2, pady=20)

        # Transaction Frame
        self.transaction_frame = tk.Frame(self, bg="#2C3E50")

        # Header
        tk.Label(self.transaction_frame, text="Account Operations", font=("Arial", 16, "bold"), 
                bg="#2C3E50", fg="#ECF0F1").pack(pady=10)

        # Account Info
        self.info_label = tk.Label(self.transaction_frame, font=("Arial", 12), 
                                 bg="#2C3E50", fg="#BDC3C7")
        self.info_label.pack()

        # Balance Display
        self.balance_label = tk.Label(self.transaction_frame, font=("Arial", 14, "bold"), 
                                    bg="#2C3E50", fg="#27AE60")
        self.balance_label.pack(pady=10)

        # Amount Entry
        amount_frame = tk.Frame(self.transaction_frame, bg="#2C3E50")
        amount_frame.pack(pady=10)
        tk.Label(amount_frame, text="Amount:", font=("Arial", 12), 
                bg="#2C3E50", fg="#BDC3C7").pack(side=tk.LEFT, padx=5)
        self.amount_entry = tk.Entry(amount_frame, font=("Arial", 12), width=15)
        self.amount_entry.pack(side=tk.LEFT, padx=5)

        # Buttons
        button_frame = tk.Frame(self.transaction_frame, bg="#2C3E50")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Debit", command=self.debit, font=("Arial", 12, "bold"),
                 bg="#E74C3C", fg="white", width=8, relief="flat").grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Credit", command=self.credit, font=("Arial", 12, "bold"),
                 bg="#27AE60", fg="white", width=8, relief="flat").grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Balance", command=self.check_balance, font=("Arial", 12, "bold"),
                 bg="#2980B9", fg="white", width=8, relief="flat").grid(row=0, column=2, padx=10)
        tk.Button(button_frame, text="Exit", command=self.destroy, font=("Arial", 12, "bold"),
                 bg="#7F8C8D", fg="white", width=8, relief="flat").grid(row=0, column=3, padx=10)

        # Message Label
        self.message_label = tk.Label(self.transaction_frame, font=("Arial", 12), 
                                    bg="#2C3E50", wraplength=400)
        self.message_label.pack(pady=10)

    def create_account(self):
        acc_no = self.acc_entry.get().strip()
        bal_str = self.bal_entry.get().strip()
        
        if not acc_no:
            messagebox.showerror("Error", "Account number cannot be empty!")
            return
            
        try:
            balance = float(bal_str)
            if balance < 0:
                raise ValueError
            self.account = Account(balance, acc_no)
            self.setup_frame.pack_forget()
            self.transaction_frame.pack(pady=20)
            self.info_label.config(text=f"Account Number: {acc_no}")
            self.update_balance()
        except ValueError:
            messagebox.showerror("Error", "Invalid initial balance!\nPlease enter a positive number.")

    def update_balance(self):
        balance = self.account.get_balance()
        self.balance_label.config(text=f"Current Balance: ₹{balance:.2f}")

    def debit(self):
        amount_str = self.amount_entry.get()
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError
            success, message = self.account.debit(amount)
            self.update_balance()
            self.amount_entry.delete(0, tk.END)
            color = "#2ECC71" if success else "#E74C3C"
            self.message_label.config(text=message, fg=color)
        except ValueError:
            self.message_label.config(text="Invalid amount!\nPlease enter positive numbers only.", fg="#E74C3C")

    def credit(self):
        amount_str = self.amount_entry.get()
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError
            success, message = self.account.credit(amount)
            self.update_balance()
            self.amount_entry.delete(0, tk.END)
            self.message_label.config(text=message, fg="#2ECC71")
        except ValueError:
            self.message_label.config(text="Invalid amount!\nPlease enter positive numbers only.", fg="#E74C3C")

    def check_balance(self):
        balance = self.account.get_balance()
        self.message_label.config(text=f"Current Available Balance: ₹{balance:.2f}", fg="#3498DB")

if __name__ == "__main__":
    app = BankApp()
    app.mainloop()