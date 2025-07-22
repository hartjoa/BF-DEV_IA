from Models.character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()
        self.__visible = False
    
    @property
    def visible(self):
        return self.__visible
    
    @visible.setter
    def visible(self, value):
        self.__visible = value

    def give_resources(self, character):
        for resource, amount in self.inventory.items():
            if resource in character.inventory:
                character.inventory[resource] +=  amount
            else:
                character.inventory[resource] = amount

