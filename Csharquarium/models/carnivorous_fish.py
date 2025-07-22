from models.fish import Fish
from abc import abstractmethod

class CarnivorousFish(Fish):
    def __init(self, name: str, gender: str) -> None:
        super().__init__(name, gender)

    def eat(self, fish: Fish) -> None:
        if isinstance(fish, Fish):
            print(f"{self.name} is eating some good fish! RIP {fish.name}...")
        else:
            print(f"Sorry... That ain't no good food for {self.name}")
    
    def __str__(self) -> None:
        return super().__str__("Carni")