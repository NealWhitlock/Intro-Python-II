# Implement a class to hold room information. This should have name and
# description attributes.
#from item import Item

class Room:
    def __init__(self, name, description, items_list=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items_list = items_list
    
    def remove_item(self, item):
        self.items_list.remove(item)
    
    def add_item(self, item):
        self.items_list.append(item)
