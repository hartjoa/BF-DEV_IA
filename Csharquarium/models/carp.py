from .herbivorous_fish import HerbivorousFish
from .fish import Fish, Sexualities

class Carp(HerbivorousFish):
    def __init__(self, **kwargs) -> None:
        super().__init__(sexuality=Sexualities.MONOSEXUAL, **kwargs)
    
    def mate(self, other: Fish) -> Fish:
        return super().mate(other)