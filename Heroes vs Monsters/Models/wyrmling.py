from Models.monster import Monster
from Models.dice import Dice
import constants as k

class Wyrmling(Monster):    # Dragonnet
    def __init__(self):
        super().__init__()
        self.__bonus_endurance = 1
        self.inventory[k.GOLD] = Dice(1, 6).roll()
        self.inventory[k.LEATHER] = Dice(1, 4).roll()

    @property
    def end(self):
        return super().end + self.__bonus_end

    def show_info(self):
        print("DRAGONNET")
        super().show_info()
    
    def __str__(self):
        return "💀" if self.dead else "🐉"
