from player import Player
from room import Room
from item import Item
import textwrap

# Declare all the rooms via a map_layout dictionary

map_layout = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons", [Item('pebble', 'desc'), Item('map', 'desc')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('torch', 'desc')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('shield', 'desc'), Item('dessert', 'desc')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('rock', 'desc')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('hope', 'desc')]),
}


# Link rooms together. These create connections by replacing the None when 
# the instance of a given room is created in the dictionary above.

map_layout['outside'].n_to = map_layout['foyer']
map_layout['foyer'].s_to = map_layout['outside']
map_layout['foyer'].n_to = map_layout['overlook']
map_layout['foyer'].e_to = map_layout['narrow']
map_layout['overlook'].s_to = map_layout['foyer']
map_layout['narrow'].w_to = map_layout['foyer']
map_layout['narrow'].n_to = map_layout['treasure']
map_layout['treasure'].s_to = map_layout['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Neal", map_layout["outside"])

print(player.current_room.items_list)

# Write a loop that:
playing = True
while playing:
    #
    # * Prints the current room name
    print(player)
    # * Prints the current description (the textwrap module might be useful here).
    for line in textwrap.wrap(player.current_room.description, 50):
        print(line)
    #print(player.current_room.description)
    if player.current_room.items_list:
        print("The room you are in contains the following:")
        for item in player.current_room.items_list:
            print(item)
        print()
    # * Waits for user input and decides what to do.
    direction = ['placeholder']
    while direction[0] not in ['q', 'n', 's', 'e', 'w', 'get', 'take', 'drop']:
        direction = input("Please choose a direction ('n','s','e','w') or interact with an item. ('q' to quit):").split()
        if len(direction) == 1:
            # Change Rooms
            in_place = player.current_room.name
            #
            # If the user enters "q", quit the game.
            if direction[0] == 'q':
                print("Terminating game session")
                playing = False
            elif direction[0] == 'i' or direction == 'inventory':
                print(player.inventory)
            #
            # If the user enters a cardinal direction, attempt to move to the room there.
            # Print an error message if the movement isn't allowed.
            elif direction[0] == 'n':
                if player.current_room.n_to:
                    player.current_room = player.current_room.n_to
            elif direction[0] == 's':
                if player.current_room.s_to:
                    player.current_room = player.current_room.s_to
            elif direction[0] == 'e':
                if player.current_room.e_to:
                    player.current_room = player.current_room.e_to
            elif direction[0] == 'w':
                if player.current_room.w_to:
                    player.current_room = player.current_room.w_to

            if (player.current_room.name == in_place) and (direction[0] != 'q') and (direction[0] != 'i'):
                print("That is not a valid movement at this time.")
            
            print()
        elif len(direction) == 2:
            print()
            print(direction[1])
            print(player.current_room.items_list)
            print(f"{direction[1]} is type {type(player.current_room.items_list[0])}")
            print()

            no_item = True
            for item in player.current_room.items_list: 
                if direction[1] == item.name:
                    # Do something with item
                    if (direction[0] == 'get') or (direction[0] == 'take'):
                        player.pickup_item(direction[1])
                        player.current_room.remove_item(direction[1])
                        item.on_take(direction[1])
                        no_item = False
                    else:
                        player.drop_item(direction[1])
                        player.current_room.add_item(direction[1])
                        item.on_drop(direction[1])
                        no_item = False

            if no_item:
                print("No such item at your location.")
                print()





            # # Do Action
            # if direction[1] in player.current_room.items_list:
            #     # Do something with item
            #     if (direction[0] == 'get') or (direction[0] == 'take'):
            #         player.pickup_item(direction[1])
            #         player.current_room.remove_item(direction[1])
            #         item.on_take(direction[1])
            #     else:
            #         player.drop_item(direction[1])
            #         player.current_room.add_item(direction[1])
            #         item.on_drop(direction[1])
            # else:
            #     print("No such item at your location.")

    



