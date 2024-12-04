# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:21:12 2024

@author: SATHISH S
"""

class Weather:
    def __init__(self, location, temperature, humidity):
        self.location = location
        self.temperature = temperature
        self.humidity = humidity

    def update_weather(self, temp, hum):
        self.temperature = temp
        self.humidity = hum

    def display_weather(self):
        print(f"Weather Report for {self.location}")
        print(f"Temperature: {self.temperature}°C")
        print(f"Humidity: {self.humidity}%")

# Example usage:
weather = Weather("Coimbatore", 30, 70)
weather.display_weather()
weather.update_weather(32, 65)
weather.display_weather()
