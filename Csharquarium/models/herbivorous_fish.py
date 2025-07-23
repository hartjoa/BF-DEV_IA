from models.fish import Fish
from models.alga import Alga
from abc import abstractmethod

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
    
    def __str__(self) -> str:
        return super().__str__("Herbi")