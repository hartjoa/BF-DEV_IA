from abc import abstractmethod
from models.aquatic_organism import AquaticOrganism
from utils import Utils
from colorama import Fore

import random
SEXUAL_MATURITY = 3

class Fish(AquaticOrganism):
    def __init__(self, name: str, gender: str) -> None:
        super().__init__()
        self.name = name
        self.gender = "F" if gender and gender[0].upper() == "F" else "M"
    
    @abstractmethod
    def eat(self, food):
        pass
    
    @staticmethod
    def generate(tp: type) -> "tp":
        if not issubclass(tp, Fish):
            raise TypeError("Only fishes can be instanciated with the 'generate' method")
        name = f"{tp.__name__}-{random.randint(1, 1_000_000_000)}"
        gender = random.choice(["Male", "Female"])
        return tp(name, gender)
        

    def mate(self, other: "Fish") -> None:
        if self.age < SEXUAL_MATURITY:
            return None
        is_mate_possible = True
        print(f"{self.name} is trying to mate with {other.name}")
        if other.age < SEXUAL_MATURITY:
            print(f"{other.name} is too young to mate!")
            is_mate_possible = False
        if type(self) != type(other):
            print(f"A {self.__class__.__name__} cannot mate with a {other.__class__.__name__}!")
            is_mate_possible = False
        if self.gender == other.gender:
            print(f"Two {'males' if self.gender == 'M' else 'females'} cannot mate together!")
            is_mate_possible = False
        if is_mate_possible:
            Utils.nice_print("A baby fish is born! Welcome to:")
            baby_fish = Fish.generate(type(self))
            Utils.nice_print(baby_fish, Fore.MAGENTA)
            return baby_fish
        return None
    
    def __str__(self, fish_type: str) -> str:
        return f"{self.name} ({self.gender[0].upper()}), {self.age} days: {self.__class__.__name__} ({fish_type})[{self.pv} pv] -- {'🐠' if self.is_alive else '💀'}"