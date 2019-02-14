# Write a class to hold player information, e.g. what room they are in
# currently.
import item

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = [item.Sword]

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def __repr__(self):
        return f"Player is in {self.current_room}"
