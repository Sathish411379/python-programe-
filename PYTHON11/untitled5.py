# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:18:58 2024

@author: SATHISH S
"""
class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            print(f"{book} has been borrowed.")
        else:
            print(f"{book} is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{book} has been returned.")
        else:
            print(f"{book} was not borrowed.")

    def display_borrowed_books(self):
        if not self.borrowed_books:
            print("No books borrowed.")
        else:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book}")

# Example usage:
member = Member("John Doe", 101)
member.borrow_book("The Great Gatsby")
member.borrow_book("1984")
member.display_borrowed_books()
member.return_book("1984")
member.display_borrowed_books()

