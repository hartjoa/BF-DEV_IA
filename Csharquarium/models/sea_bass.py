from .herbivorous_fish import HerbivorousFish
from .fish import Fish, Sexualities

class SeaBass(HerbivorousFish):
    def __init__(self, **kwargs) -> None:
        super().__init__(sexuality=Sexualities.AGE_BASED_HERMAPHRODITE, **kwargs)
    
    def mate(self, other: Fish) -> Fish:
        return super().mate(other)