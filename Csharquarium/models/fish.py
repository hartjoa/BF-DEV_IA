from abc import abstractmethod
from models.aquatic_organism import AquaticOrganism
import random

SEXUAL_MATURITY = 3

class Fish(AquaticOrganism):
    def __init__(self, name, gender):
        super().__init__()
        self.name = name
        self.gender = "F" if gender and gender[0].upper() == "F" else "M"
    
    @abstractmethod
    def eat(self, food):
        pass

    def mate(self, other):
        if self.age < SEXUAL_MATURITY:
            return None
        
        print(f"*** {self.name} is trying to mate with {other.name}")
        if other.age < SEXUAL_MATURITY:
            print(f"{other.name} is too young to mate!")
        elif type(self) != type(other):
            print(f"A {self.__class__.__name__} cannot mate with a {other.__class__.__name__}!")
        elif self.gender == other.gender:
            print(f"Two {'males' if self.gender == 'M' else 'females'} cannot mate together!")
        else:
            print("*** A baby fish is born! Welcome to:")
            baby_fish = type(self)(f"baby-{random.randint(1, 1_000_000)}", "M" if random.random() < .5 else "F")
            print(baby_fish)
            return baby_fish
        return None
    
    def __str__(self, fish_type):
        return f"{self.name} ({self.gender[0].upper()}), {self.age} days: {self.__class__.__name__} ({fish_type})[{self.pv} pv] -- {'🐠' if self.is_alive else '💀'}"