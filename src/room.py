# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def print_items(self):
        for item in self.items:
            print(item, '\n')

    def __repr__(self):
        return f"{self.name}, {self.description}"
