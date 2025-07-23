from models.fish import Fish, Sexualities
from models.alga import Alga
from abc import abstractmethod
import random

class HerbivorousFish(Fish):
    def __init__(self, name: str, gender: str, sexuality: Sexualities) -> None:
        super().__init__(name, gender, sexuality)

    def eat(self, alga: Alga, verbose: bool = False) -> None:
        if isinstance(alga, Alga):
            if verbose:
                print(f"{self.name} is eating some good alga!")
            # alga is harmed
            alga.pv -= 2
            if verbose:
                print(f"Alga loses 2 pv => {alga.pv}")
            # fish is fed
            self.pv += 3
            if verbose:
                print(f"Delicious! {self.name} won 3pv => {self.pv}")
        else:
            if verbose:
                print(f"Sorry... That ain't no good food for {self.name}")
    
    def find_alga(self, aquarium: "Aquarium", verbose: bool = False) -> Alga:
        if verbose:
            print(f"{self.name} is looking for an alga to eat...")
        if len(aquarium.algae) == 0:
            # no more alga in the aquarium
            if verbose:
                print(f"There's no more alga left to feed you, poor {self.name}")
            return None
        else:
            return random.choice(aquarium.algae)