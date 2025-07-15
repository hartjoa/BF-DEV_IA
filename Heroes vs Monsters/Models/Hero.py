from Models.character import Character

class Hero(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def __str__(self):
        return "H"