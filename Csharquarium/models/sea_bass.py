from .herbivorous_fish import HerbivorousFish
from .fish import Fish, Sexualities

class SeaBass(HerbivorousFish):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.sexuality=Sexualities.AGE_BASED_HERMAPHRODITE
    
    def mate(self, other: Fish, verbose: bool = False) -> Fish:
        return super().mate(other, verbose)