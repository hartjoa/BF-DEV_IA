import random

class Dice:
    def __init__(self, minimum, maximum):
        self.__minimium = minimum
        self.__maximum = maximum

    def roll(self):
        return random.randint(self.__minimium, self.__maximum)
