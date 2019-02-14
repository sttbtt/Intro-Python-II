from room import Room

# Declare all the rooms

room = {
    'outside':  Room("\nOutside Cave Entrance",
"""North of you, the cave mount beckons"""),

    'foyer':    Room("\nFoyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("\nGrand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("\nNarrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("\nTreasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# # Declare all items

# item = {
#     'sword': Item("Sword", "Large sharp sword"),
#     'knife': Item("Knife", "A pointy knife"),
#     'axe': Item("Axe", "A dull axe"),
#     'coins': Item("Coins", "Shinny golden coins"),
#     'rock': Item("Rock", "Yes, a rock")

# }