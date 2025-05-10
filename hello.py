import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'

    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        if Path(self.database).exists():
            try:
                with open(self.database, 'r') as fs:
                    return json.load(fs)
            except Exception as err:
                print(f"Error loading data: {err}")
                return []
        else:
            print("No data file found. Starting with empty database.")
            return []

    def update_data(self):
        with open(self.database, 'w') as fs:
            json.dump(self.data, fs, indent=4)

    def generate_account_id(self):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def create_account(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        email = input("Enter your email: ")
        pin = input("Enter your 4-digit PIN: ")

        if age < 18 or len(pin) != 4 or not pin.isdigit():
            print("Account creation failed. Invalid age or PIN.")
            return

        account_id = self.generate_account_id()
        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "accountNo": account_id,
            "balance": 0
        }

        self.data.append(account)
        self.update_data()
        print(f"Account created successfully! Your Account Number is {account_id}")

    def find_user(self, acc_num, pin):
        return next((user for user in self.data if user["accountNo"] == acc_num and user["pin"] == pin), None)

    def deposit_money(self):
        acc = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))
        user = self.find_user(acc, pin)

        if not user:
            print("No matching account found.")
            return

        amount = int(input("Enter amount to deposit: "))
        if amount <= 0 or amount > 10000:
            print("Invalid amount. Must be between 1 and 10000.")
            return

        user["balance"] += amount
        self.update_data()
        print("Amount deposited successfully.")

    def withdraw_money(self):
        acc = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))
        user = self.find_user(acc, pin)

        if not user:
            print("No matching account found.")
            return

        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0 or amount > user["balance"]:
            print("Insufficient balance or invalid amount.")
            return

        user["balance"] -= amount
        self.update_data()
        print("Amount withdrawn successfully.")

    def show_details(self):
        acc = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))
        user = self.find_user(acc, pin)

        if not user:
            print("No matching account found.")
            return

        print("\nYour Account Details:")
        for k, v in user.items():
            print(f"{k.capitalize()}: {v}")

    def update_details(self):
        acc = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))
        user = self.find_user(acc, pin)

        if not user:
            print("No matching account found.")
            return

        print("Leave any field blank to keep it unchanged.")
        name = input("New name: ") or user["name"]
        email = input("New email: ") or user["email"]
        pin_input = input("New 4-digit PIN: ")

        if pin_input and (len(pin_input) != 4 or not pin_input.isdigit()):
            print("Invalid PIN format. Update cancelled.")
            return

        user["name"] = name
        user["email"] = email
        if pin_input:
            user["pin"] = int(pin_input)

        self.update_data()
        print("Details updated successfully.")

    def delete_account(self):
        acc = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))
        user = self.find_user(acc, pin)

        if not user:
            print("No matching account found.")
            return

        confirm = input("Are you sure you want to delete your account? (y/n): ")
        if confirm.lower() == 'y':
            self.data.remove(user)
            self.update_data()
            print("Account deleted successfully.")
        else:
            print("Deletion cancelled.")


def main():
    bank = Bank()
    while True:
        print("\n--- Welcome to Console Bank ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show Details")
        print("5. Update Details")
        print("6. Delete Account")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.deposit_money()
        elif choice == '3':
            bank.withdraw_money()
        elif choice == '4':
            bank.show_details()
        elif choice == '5':
            bank.update_details()
        elif choice == '6':
            bank.delete_account()
        elif choice == '7':
            print("Thank you for using Console Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
