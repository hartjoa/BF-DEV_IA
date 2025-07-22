from models.herbivorous_fish import HerbivorousFish
from models.fish import Fish

class Carp(HerbivorousFish):
    def __init__(self, name: str, gender: str) -> None:
        super().__init__(name, gender)
    
    def mate(self, other: Fish) -> Fish:
        return super().mate(other)