# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:09:56 2024

@author: SATHISH S
"""

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title):
        if title in self.books:
            print(f"The book '{title}' is already in the library.")
        else:
            self.books[title] = 'available'
            print(f"The book '{title}' has been added to the library.")

    def borrow_book(self, title):
        if title in self.books:
            if self.books[title] == 'available':
                self.books[title] = 'borrowed'
                print(f"You have borrowed '{title}'.")
            else:
                print(f"Sorry, the book '{title}' is currently borrowed.")
        else:
            print(f"Sorry, the book '{title}' is not in the library.")

    def return_book(self, title):
        if title in self.books:
            if self.books[title] == 'borrowed':
                self.books[title] = 'available'
                print(f"You have returned '{title}'.")
            else:
                print(f"The book '{title}' was not borrowed.")
        else:
            print(f"Sorry, the book '{title}' is not in the library.")

    def view_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            for title, status in self.books.items():
                print(f"Title: '{title}', Status: {status}")

# Example usage:
library = Library()
library.add_book('The Great Gatsby')
library.add_book('1984')
library.view_books()
library.borrow_book('1984')
library.view_books()
library.return_book('1984')
library.view_books()
