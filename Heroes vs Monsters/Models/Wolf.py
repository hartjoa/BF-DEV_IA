from Models.monster import Monster
from Models.dice import Dice

class Wolf(Monster):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.leather = Dice(1, 4).roll()

    def show_info(self):
        print("LOUP")
        super().show_info()
    
    def __str__(self):
        return "🐺"