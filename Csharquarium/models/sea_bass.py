from .herbivorous_fish import HerbivorousFish
from .fish import Fish, Sexualities

class SeaBass(HerbivorousFish):
    def __init__(self, name: str, gender: str) -> None:
        super().__init__(name, gender, Sexualities.AGE_BASED_HERMAPHRODITE)
    
    def mate(self, other: Fish) -> Fish:
        return super().mate(other)