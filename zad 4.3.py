# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property - Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}, Address: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House - {super().__str__()}, Plot: {self.plot}"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat - {super().__str__()}, Floor: {self.floor}"


# Przykładowe użycie
house_obj = House(area=43-600, rooms=4, price=550000, address="123 Ulicowa", plot=500)
flat_obj = Flat(area=43-603, rooms=2, price=150000, address="456 Ulicna", floor=2)

print(house_obj)
print(flat_obj)
