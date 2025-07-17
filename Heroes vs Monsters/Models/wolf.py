from Models.monster import Monster
from Models.dice import Dice
import constants as k

class Wolf(Monster):
    def __init__(self):
        super().__init__()
        self.inventory[k.LEATHER] = Dice(1, 4).roll()

    def show_info(self):
        print("LOUP")
        super().show_info()
    
    def __str__(self):
        return "💀" if self.dead else "🐺"
