# Imports
from my_functions import *
from room import Room
from player import Player
from item import *
from data import *

#
# Main
#

clear()
print('N -> North, S -> South, E -> East, W -> West\nL -> List room items, I -> Show your inventory\nget \'item\', drop \'item\'\nh -> Help, q -> Quit\n')

# Make a new player object that is currently in the 'outside' room.
player = Player("Scott", room['outside'], [])
room['outside'].items.append(item['sword'])
room['outside'].items.append(item['knife'])
room['foyer'].items.append(item['knife'])
room['overlook'].items.append(item['rock'])
room['narrow'].items.append(item['axe'])
room['treasure'].items.append(item['coin'])
# player.items.append(item['sword'])
# player.items.append(item['knife'])
# player.items.append(item['rock'])
# player.items.append(item['axe'])

# Write a loop that:
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.

while True:
    # * Prints the current room name
    print('\nLocation:')
    print(player.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
 
    # * Waits for user input and decides what to do.
    s = input("\n> ").lower().split()

    if len(s) == 1:
        s = s[0][0]

        if s == 'q':
            print("See you next time!")
            break
        
        if s == 'l':
            player.current_room.print_items()
            continue

        if s == 'i':
            player.print_inventory()
            continue
            
        if s == 'h':
            print('N -> North, S -> South, E -> East, W -> West\nL -> List room items, I -> Show your inventory\nget \'item\', drop \'item\'\nh -> Help, q -> Quit\n')
        
        if s == 'n' or s == 's' or s == 'e' or s == 'w':
            player.current_room = try_direction(s, player.current_room)
        else:
            print("I don't understand that direction.")
        continue

    elif len(s) == 2:
        action = s[0]
        the_item = s[1]
        # print(action, the_item)
        # print(player.current_room.items)
        # print(player.items.count("Sword"))
        

        if action in ['get', 'drop']:
            if action == 'get':
                player.get_item(the_item)
                # TODO figure out if the_item is in items
                # if the_item == the_item:
                #     player.items.append(item[the_item])
                #     player.current_room.items.remove(item[the_item])
                #     # TODO add on_take
                # else:
                #     print("That item is not in this room.")
            elif action == 'drop':
                player.drop_item(the_item)
                # # TODO figure out if the_item is in items
                # if the_item == the_item:
                #     player.items.remove(item[the_item])
                #     player.current_room.items.append(item[the_item])
                #     # TODO add on_drop
                # else:
                #     print("You don't have the item.")
        else:
            print("I don't understand that.")
    
    else:
        print("I don't understand that.")
        continue



