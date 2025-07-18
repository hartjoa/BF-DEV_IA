from models.carnivorous_fish import CarnivorousFish

class Clownfish(CarnivorousFish):
    def __init__(self, name, gender):
        super().__init__(name, gender)

    def mate(self, other):
        pass