from models.fish import Fish
from abc import abstractmethod

class CarnivorousFish(Fish):
    def __init(self, name, gender):
        super().__init__(name, gender)

    def eat(self, fish):
        if isinstance(fish, Fish):
            print(f"{self.name} is eating some good fish! RIP {fish.name}...")
        else:
            print(f"Sorry... That ain't no good food for {self.name}")
    
    def __str__(self):
        return f"{self.name} ({self.gender[0].upper()}): {self.__class__.__name__} (carnivorous) [{self.pv} pv] -- {'alive' if self.is_alive else 'dead'}"