from .herbivorous_fish import HerbivorousFish
from .fish import Fish, Sexualities

class Carp(HerbivorousFish):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.sexuality=Sexualities.MONOSEXUAL
    
    def mate(self, other: Fish, verbose = False) -> Fish:
        return super().mate(other, verbose)