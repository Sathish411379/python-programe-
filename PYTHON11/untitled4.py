# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:17:49 2024

@author: SATHISH S
"""

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary:.2f}")

    def give_raise(self, percent):
        self.salary += self.salary * (percent / 100)
        print(f"Salary increased by {percent}%. New Salary: ${self.salary:.2f}")

# Example usage:
employee1 = Employee("Alice Smith", 101, 50000)
employee1.display_details()
employee1.give_raise(10)
employee1.display_details()
