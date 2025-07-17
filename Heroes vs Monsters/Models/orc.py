from Models.monster import Monster
from Models.dice import Dice
import constants as k

class Orc(Monster):
    def __init__(self):
        super().__init__()
        self.__bonus_force = 1
        self.inventory[k.GOLD] = Dice(1, 6).roll()

    @property
    def force(self):
        return super().force + self.__bonus_force

    def show_info(self):
        print("ORQUE")
        super().show_info()
    
    def __str__(self):
        return "💀" if self.dead else "👹"
