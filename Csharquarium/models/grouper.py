from models.carnivorous_fish import CarnivorousFish

class Grouper(CarnivorousFish):
    def __init__(self, name, gender):
        super().__init__(name, gender)
    
    def mate(self, other):
        super().mate(other)