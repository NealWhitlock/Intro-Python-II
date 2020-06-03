class Student:
    def __init__(self, first_name, last_name):
        # What happens when an instance is created
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        # What gets returned when printing with calling a given instance
        # print(me)  <-- printed
        # Without this you will return the instance's location in memory
        return f"This student's name is {self.first_name}, {self.last_name}."
    
    def __repr__(self):
        # Returns a printable version of the method
        # me  <-- not printed, just called
        return f"Could return info here on how the object is created."
        # f"Point (x={self.x}, y={self.y})"  # From lecture


me = Student("Neal", "Whitlock")
print(me)
