# Clear Screen
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()

from room import Room
from player import Player
from data import *

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Scott", room['outside'])

def try_direction(direction, current_room):
    attribute = direction + '_to'

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print("Invalid direction!")
        return current_room

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.

while True:
    
    print(player.current_room.name)
    print(player.current_room.description)
    s = input("\n> ").lower().split()

    if len(s) == 1:
        s = s[0][0]

        if s == 'q':
            print("See you next time!")
            break
        
        if s == 'l':
            print(item)

        if s == 'i':
            print(player.inventory)
        
        player.current_room = try_direction(s, player.current_room)

    elif len(s) == 2:
        first_word = s[0]
        second_word = s[1]

        if first_word in ['get', 'drop']:
            print(first_word, second_word)
    
    else:
        print("I don't understand that.")
        continue



