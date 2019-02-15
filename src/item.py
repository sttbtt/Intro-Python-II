class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'You picked up {self.name}.')

    def on_drop(self):
        print(f'You dropped {self.name}.')

    def __repr__(self):
        return f"{self.name} - {self.description}"


class Weapon(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name} - {self.description}"

