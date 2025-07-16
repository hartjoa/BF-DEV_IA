from Models.monster import Monster
from Models.dice import Dice

class Wyrmling(Monster):    # Dragonnet
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__bonus_end = 1
        self.gold = Dice(1, 6).roll()
        self.leather = Dice(1, 4).roll()

    @property
    def end(self):
        return super().end + self.__bonus_end

    def show_info(self):
        print("DRAGONNET")
        super().show_info()
    
    def __str__(self):
        return "🐉"
