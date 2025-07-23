from models.carnivorous_fish import CarnivorousFish
from models.fish import Fish, Sexualities

class Clownfish(CarnivorousFish):
    def __init__(self, name: str, gender: str) -> None:
        super().__init__(name, gender, Sexualities.OPPORTUNISTIC_HERMAPHRODITE)

    def mate(self, other: Fish) -> Fish:
        return super().mate(other)