from .carnivorous_fish import CarnivorousFish
from .fish import Fish, Sexualities

class Tuna(CarnivorousFish):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.sexuality=Sexualities.MONOSEXUAL
    
    def mate(self, other: Fish, verbose: bool = False) -> Fish:
        return super().mate(other, verbose)