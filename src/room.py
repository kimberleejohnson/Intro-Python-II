# Class to hold room information.
# Includes name, description, 
# And a directional attribute set to none because it's specified in adv.py
# This is not assigned as a parameter here in this class because it's adv.py 


class Room:
   # Declares attributes 
   def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None 
        self.w_to = None 