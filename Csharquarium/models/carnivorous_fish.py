from .fish import Fish, Sexualities
from abc import abstractmethod
import random

class CarnivorousFish(Fish):
    def __init(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def eat(self, prey: Fish, verbose: bool = False) -> None:
        if isinstance(prey, Fish):
            if verbose:
                print(f"Hmm... That's {prey.name} over there! Should I eat you?")
            if type(prey) == type(self):
                # cannot eat a fish like you
                if verbose:
                    print(f"{self.name} won't eat its conspecific! Have a good day, {prey.name}")
            else:
                # prey is harmed
                prey.pv -= 4
                if verbose:
                    print(f"{prey.name} loses 4 pv => {prey.pv}")
                # fish is fed
                self.pv += 5
                if verbose:
                    print(f"Delicious! I liked you very much, {prey.name}! {self.name} won 5pv => {self.pv}")
        else:
            if verbose:
                print(f"Sorry... That ain't no good food for {self.name}")
    
    def find_prey(self, aquarium: "Aquarium", verbose: bool = False) -> Fish:
        if verbose:
            print(f"{self.name} is looking for a fish to eat...")
        if len(aquarium.fishes) < 2:
            # only fish in the aquarium
            if verbose:
                print(f"There's no more fish left to feed you, poor {self.name}")
            return None
        else:            
            # find a prey and eat it
            return random.choice([target for target in aquarium.fishes if target != self])