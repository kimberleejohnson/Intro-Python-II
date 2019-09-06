# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, current_room): 
        self.name = name
        self.current_room = current_room 
    
    # Returns the string definition of the object, we need it in order to print things. 
    def __str__(self):
        s = f"Your player {self.name} is in the {self.current_room} room."
        return s
    
    def __repr__(self): 
        return f"Your player {self.name} is in the {self.current_room} room."