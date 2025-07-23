from .carnivorous_fish import CarnivorousFish
from .fish import Fish, Sexualities

class Grouper(CarnivorousFish):
    def __init__(self, name: str, gender: str) -> None:
        super().__init__(name, gender, Sexualities.AGE_BASED_HERMAPHRODITE)
    
    def mate(self, other: Fish) -> Fish:
        return super().mate(other)