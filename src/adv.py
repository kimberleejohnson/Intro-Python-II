# Importing sys so it will be easy to exit out 
import sys 
from player import Player 
from room import Room

# Declare all the rooms, as instances of the Room Class in a dictionary called "room"

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
 passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
 into the darkness. Ahead to the north, a light flickers in
 the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
 to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
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

#
# Main
#

# New player object that is currently in the 'outside' room.
playerOne = Player("Kimberlee", 'outside')

# Setting up Boolean for status of game
active_session = True

# Write a loop ('REPL parser' from the instructions) that, while the session is active:
while active_session: 
   
   # Prints the current room name and description
   # Room for improvement: print these as string literals 
   print("You are in the...")
   print(room[playerOne.current_room].name)
   print("...")
   print(room[playerOne.current_room].description)

   # * Waits for user input and decides what to do.
   user_direction = input("Enter a cardinal direction the player should move to \n n for North \n e for East \n s for South \n w for West \n q to Quit \n Your input: ").lower()

   # If the user enters "q", quit the game.
   if user_direction == 'q': 
      print("Thanks for playing. Goodbye!")
      sys.exit(1)
   
   # If the user enters a cardinal direction, attempt to move to the room there.
   if user_direction == 'n': 
      room[playerOne.current_room] = room[playerOne.current_room].n_to

   # Print an error message if the movement isn't allowed.
