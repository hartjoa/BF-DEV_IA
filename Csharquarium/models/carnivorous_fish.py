from models.fish import Fish
from abc import abstractmethod

class CarnivorousFish(Fish):
    def __init(self, name: str, gender: str) -> None:
        super().__init__(name, gender)

    def eat(self, prey: Fish) -> None:
        if isinstance(prey, Fish):
            print(f"Hmm... That's {prey.name} over there! Should I eat you?")
            if type(prey) == type(self):
                # cannot eat a fish like you
                print(f"{self.name} won't eat its conspecific! Have a good day, {prey.name}")
            else:
                # prey is harmed
                prey.pv -= 4
                print(f"{prey.name} loses 4 pv => {prey.pv}")
                # fish is fed
                self.pv += 5
                print(f"Delicious! I liked you very much, {prey.name}! {self.name} won 5pv => {self.pv}")
        else:
            print(f"Sorry... That ain't no good food for {self.name}")
    
    def __str__(self) -> None:
        return super().__str__("Carni")