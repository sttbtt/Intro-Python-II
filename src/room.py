# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, desciption):
        self.name = name
        self.desciption = desciption

    def __repr__(self):
        return f"{self.name}, {self.desciption}"
