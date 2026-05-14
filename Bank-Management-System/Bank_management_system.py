import json

class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Account Balance for {self.name} (Acc No: {self.acc_no}): ₹{self.balance}")

    def to_dict(self):
        return {
            "acc_no": self.acc_no,
            "name": self.name,
            "balance": self.balance
        }


class BankSystem:
    def __init__(self):
        self.accounts = self.load_accounts()

    def load_accounts(self):
        try:
            with open("accounts.json", "r") as f:
                data = json.load(f)
                return [Account(**acc) for acc in data]
        except FileNotFoundError:
            return []

    def save_accounts(self):
        with open("accounts.json", "w") as f:
            json.dump([acc.to_dict() for acc in self.accounts], f, indent=4)

    def find_account(self, acc_no):
        for acc in self.accounts:
            if acc.acc_no == acc_no:
                return acc
        return None

    def create_account(self):
        acc_no = input("Enter New Account Number: ")
        if self.find_account(acc_no):
            print(" Account number already exists.")
            return
        name = input("Enter Account Holder Name: ")
        acc = Account(acc_no, name)
        self.accounts.append(acc)
        self.save_accounts()
        print(" Account created successfully.")

    def perform_deposit(self):
        acc_no = input("Enter Account Number: ")
        acc = self.find_account(acc_no)
        if acc:
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                acc.deposit(amount)
                self.save_accounts()
            except ValueError:
                print("Invalid input. Enter a number.")
        else:
            print(" Account not found.")

    def perform_withdrawal(self):
        acc_no = input("Enter Account Number: ")
        acc = self.find_account(acc_no)
        if acc:
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                acc.withdraw(amount)
                self.save_accounts()
            except ValueError:
                print("Invalid input. Enter a number.")
        else:
            print(" Account not found.")

    def show_balance(self):
        acc_no = input("Enter Account Number: ")
        acc = self.find_account(acc_no)
        if acc:
            acc.check_balance()
        else:
            print(" Account not found.")

    def show_account_details(self):
        acc_no = input("Enter Account Number to view details: ")
        acc = self.find_account(acc_no)
        if acc:
            print("\n Account Details:")
            print(f"Account Number : {acc.acc_no}")
            print(f"Account Holder : {acc.name}")
            print(f"Account Balance: ₹{acc.balance}")
        else:
            print(" Account not found.")

    def menu(self):
        while True:
            print("\n========= Bank Management System =========")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. View Account Details")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.perform_deposit()
            elif choice == '3':
                self.perform_withdrawal()
            elif choice == '4':
                self.show_balance()
            elif choice == '5':
                self.show_account_details()
            elif choice == '6':
                self.save_accounts()
                print("Thank you for using the Bank System. Goodbye!")
                break
            else:
                print(" Invalid choice. Try again.")



bank = BankSystem()
bank.menu()
