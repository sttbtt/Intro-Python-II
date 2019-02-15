from os import system, name

# Clear Screen
def clear():
    system('cls') if name == 'nt' else system('clear')

def try_direction(direction, current_room):
    attribute = direction + '_to'

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print("Invalid direction!")
        return current_room