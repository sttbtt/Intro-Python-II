# Imports
from functions import clear
from room import Room
from player import Player
import item
from data import *

#
# Main
#

clear()
print('n -> North, s -> South, e -> East, w -> West\nl -> List room items, i -> Show your inventory\nh -> Help, q -> Quit\n')

# Make a new player object that is currently in the 'outside' room.
player = Player("Scott", room['outside'])
player.inventory.append

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
            print(f'Items in room: \n')
            
        if s == 'i':
            print(f'Your inventory: \n')
            
        if s == 'h':
            print('n -> North, s -> South, e -> East, w -> West\nl -> List room items, i -> Show your inventory\nh -> Help, q -> Quit\n')
        
        if s == 'n' or s == 's' or s == 'e' or s == 'w':
            player.current_room = try_direction(s, player.current_room)

    elif len(s) == 2:
        first_word = s[0]
        second_word = s[1]

        if first_word in ['get', 'drop']:
            print(first_word, second_word)
    
    else:
        print("I don't understand that.")
        continue



