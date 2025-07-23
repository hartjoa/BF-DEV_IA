from .carnivorous_fish import CarnivorousFish
from .fish import Fish, Sexualities

class Clownfish(CarnivorousFish):
    def __init__(self, **kwargs) -> None:
        super().__init__(sexuality=Sexualities.OPPORTUNISTIC_HERMAPHRODITE, **kwargs)

    def mate(self, other: Fish) -> Fish:
        return super().mate(other)