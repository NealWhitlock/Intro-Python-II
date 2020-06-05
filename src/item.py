# Create a file called item.py and add an Item class in there.
# The item should have name and description attributes.
# Hint: the name should be one word for ease in parsing later.

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def on_take(self, item):
        print(f"You have picked up {item}.")
    
    def on_drop(self, item):
        print(f"You have dropped {item}")

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"
    