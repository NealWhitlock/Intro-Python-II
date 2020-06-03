class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f"{self.name}\n"
        for i, cat in enumerate(self.categories):
            output += " " + str(i+1) + ". " + cat + "\n"
        
        return output

my_store = Store("Awesome Store", ["Stuff", "Other Stuff", "Yet More Stuff"])
print(my_store)

selection = input("Select the department number:")
print("The user selected " + str(selection))
