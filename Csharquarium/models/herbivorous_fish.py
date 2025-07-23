from models.fish import Fish
from models.alga import Alga
from abc import abstractmethod
import random

class HerbivorousFish(Fish):
    def __init__(self, name: str, gender: str) -> None:
        super().__init__(name, gender)

    def eat(self, alga: Alga) -> None:
        if isinstance(alga, Alga):
            print(f"{self.name} is eating some good alga!")
            # alga is harmed
            alga.pv -= 2
            print(f"Alga loses 2 pv => {alga.pv}")
            # fish is fed
            self.pv += 3
            print(f"Delicious! {self.name} won 3pv => {self.pv}")
        else:
            print(f"Sorry... That ain't no good food for {self.name}")
    
    def find_alga(self, aquarium: "Aquarium") -> Alga:
        print(f"{self.name} is looking for an alga to eat...")
        if len(aquarium.algae) == 0:
            # no more alga in the aquarium
            print(f"There's no more alga left to feed you, poor {self.name}")
            return None
        else:
            return random.choice(aquarium.algae)
    
    def __str__(self) -> str:
        return super().__str__("Herbi")