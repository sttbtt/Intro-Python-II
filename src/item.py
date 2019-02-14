class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}, {self.description}"


class Sword(Item):
    def __init__(self):
        super().__init__(name = "Sword", description = "A sharp shinny sword.")

    def __repr__(self):
        return f"{self.name}, {self.description}"