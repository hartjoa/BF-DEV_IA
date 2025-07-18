from models.herbivorous_fish import HerbivorousFish

class Carp(HerbivorousFish):
    def __init__(self, name, gender):
        super().__init__(name, gender)
    
    def mate(self, other):
        pass