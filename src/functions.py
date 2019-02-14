from os import system, name

# Clear Screen
def clear():
    system('cls') if name == 'nt' else system('clear')