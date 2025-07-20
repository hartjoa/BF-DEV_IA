from models.fish import Fish
from models.alga import Alga
from abc import abstractmethod

class HerbivorousFish(Fish):
    def __init__(self, name, gender):
        super().__init__(name, gender)

    def eat(self, alga):
        if isinstance(alga, Alga):
            print(f"{self.name} is eating some good alga!")
        else:
            print(f"Sorry... That ain't no good food for {self.name}")
    
    def __str__(self):
        return super().__str__("Herbi")