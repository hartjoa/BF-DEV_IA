from abc import abstractmethod
from models.aquatic_organism import AquaticOrganism
from utils import Utils
from colorama import Fore
from enum import Enum, auto

import random

class Sexualities(Enum):
        MONOSEXUAL = auto(),
        AGE_BASED_HERMAPHRODITE = auto(), 
        OPPORTUNISTIC_HERMAPHRODITE = auto()
    
class Fish(AquaticOrganism):
    SEXUAL_MATURITY = 3
    
    def __init__(self, name: str, gender: str, sexuality: Sexualities) -> None:
        super().__init__()
        self.sexuality = sexuality
        self.name = name
        self._gender = "F" if gender and gender[0].upper() == "F" else "M"
    
    @abstractmethod
    def eat(self, food):
        pass

    @property
    def gender(self):
        if self.sexuality == Sexualities.AGE_BASED_HERMAPHRODITE:
            return "M" if self.age <= 10 else "F"
        return self._gender
    
    @staticmethod
    def generate(tp: type) -> "tp":
        if not issubclass(tp, Fish):
            raise TypeError("Only fishes can be instanciated with the 'generate' method")
        name = f"{tp.__name__}-{random.randint(1, 1_000_000_000)}"
        gender = random.choice(["Male", "Female"])
        return tp(name, gender)

    def change_gender(self):
        self._gender = "M" if self._gender == "F" else "F"

    def mate(self, other: "Fish", verbose: bool = False) -> None:
        if self.age < Fish.SEXUAL_MATURITY:
            return None
        is_mate_possible = True
        if verbose:
            print(f"{self.name} is trying to mate with {other.name}")
        if other.age < Fish.SEXUAL_MATURITY:
            if verbose:
                print(f"{other.name} is too young to mate!")
            is_mate_possible = False
        if type(self) != type(other):
            if verbose:
                print(f"A {self.__class__.__name__} cannot mate with a {other.__class__.__name__}!")
            is_mate_possible = False
        if self.gender == other.gender:
            if self.sexuality == Sexualities.OPPORTUNISTIC_HERMAPHRODITE:
                self.change_gender()
            else:
                if verbose:
                    print(f"Two {'males' if self.gender == 'M' else 'females'} cannot mate together!")
                is_mate_possible = False
        if is_mate_possible:
            baby_fish = Fish.generate(type(self))
            Utils.nice_print(f"New born: {baby_fish}", Fore.MAGENTA)
            return baby_fish
        return None
    
    def __str__(self) -> str:
        return f"{self.name}({self.gender[0].upper()}), {self.age} days, {self.pv} pv -- {'🐠' if self.is_alive else '💀'}"