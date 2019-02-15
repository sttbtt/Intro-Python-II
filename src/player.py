from item import Item

# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items

    def print_inventory(self):
        for item in self.items:
            print(f'{item.name} - {item.description}')

    def __repr__(self):
        return f"Player is in {self.current_room}"
