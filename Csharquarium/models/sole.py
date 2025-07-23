from models.herbivorous_fish import HerbivorousFish
from models.fish import Fish, Sexualities

class Sole(HerbivorousFish):
    def __init__(self, name: str, gender: str) -> None:
        super().__init__(name, gender, Sexualities.OPPORTUNISTIC_HERMAPHRODITE)

    def mate(self, other: Fish) -> Fish:
        return super().mate(other)