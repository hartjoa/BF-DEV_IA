from .carnivorous_fish import CarnivorousFish
from .fish import Fish, Sexualities

class Grouper(CarnivorousFish):
    def __init__(self, **kwargs) -> None:
        super().__init__(sexuality=Sexualities.AGE_BASED_HERMAPHRODITE, **kwargs)
    
    def mate(self, other: Fish) -> Fish:
        return super().mate(other)