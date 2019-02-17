from item import *
from data import *

# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items

    def print_inventory(self):
        print('You have:')
        for item in self.items:
            print(f'{item.name} - {item.description}')

    def get_item(self, item_name): 
        is_avail = False   
        for my_item in self.current_room.items:
            if my_item.name.lower() == item_name:
                is_avail = True
        if is_avail:
            self.items.append(item[item_name])
            self.current_room.items.remove(item[item_name])
            print(f"You took the {item_name.capitalize()}.")
        else:
            print(f"There is not a {item_name.capitalize()} in this room.")
                
    def drop_item(self, item_name):
        is_avail = False
        for my_item in self.items:
            if my_item.name.lower() == item_name:
                is_avail = True
        if is_avail:
            self.items.remove(item[item_name])
            self.current_room.items.append(item[item_name])
            print(f"You dropped the {item_name.capitalize()}.")
        else:
            print(f"You don't have a {item_name.capitalize()}.")
     
    def __repr__(self):
        return f"Player is in {self.current_room}"
