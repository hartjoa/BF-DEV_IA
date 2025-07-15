from Models.character import Character

class Monster(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__visible = False
    
    @property
    def visible(self):
        return self.__visible
    
    @visible.setter
    def visible(self, value):
        self.__visible = value