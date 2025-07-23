from .carnivorous_fish import CarnivorousFish
from .fish import Fish, Sexualities

class Tuna(CarnivorousFish):
    def __init__(self, **kwargs) -> None:
        super().__init__(sexuality=Sexualities.MONOSEXUAL, **kwargs)
    
    def mate(self, other: Fish) -> Fish:
        return super().mate(other)