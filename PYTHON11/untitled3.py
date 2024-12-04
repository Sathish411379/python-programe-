# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:16:10 2024

@author: SATHISH S
"""

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdraw amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def view_balance(self):
        print(f"Current balance: {self.balance}")

# Example usage:
account = BankAccount("John Doe")
account.deposit(1000)
account.withdraw(250)
account.view_balance()
