from Models.Monster import Monster
from Models.Dice import Dice

class Orc(Monster):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__bonus_force = 1
        self.gold = Dice(1, 6).roll()

    @property
    def force(self):
        return super().force + self.__bonus_force

    def show_info(self):
        print("ORQUE")
        super().show_info()
    
    def __str__(self):
        return "O"
