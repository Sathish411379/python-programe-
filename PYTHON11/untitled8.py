# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:22:26 2024

@author: SATHISH S
"""

class HotelRoom:
    def __init__(self, room_number, rate_per_night):
        self.room_number = room_number
        self.is_occupied = False
        self.rate_per_night = rate_per_night

    def book_room(self):
        if not self.is_occupied:
            self.is_occupied = True
            print(f"Room {self.room_number} is now booked.")
        else:
            print(f"Room {self.room_number} is already occupied.")

    def checkout_room(self):
        if self.is_occupied:
            self.is_occupied = False
            print(f"Room {self.room_number} is now vacant.")
        else:
            print(f"Room {self.room_number} is already vacant.")

    def display_status(self):
        status = "occupied" if self.is_occupied else "vacant"
        print(f"Room Number: {self.room_number}")
        print(f"Rate per Night: ${self.rate_per_night:.2f}")
        print(f"Status: {status}")

# Example usage:
room1 = HotelRoom(101, 150.00)
room1.display_status()
room1.book_room()
room1.display_status()
room1.checkout_room()
room1.display_status()
