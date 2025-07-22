from models.carnivorous_fish import CarnivorousFish
from models.fish import Fish

class Tuna(CarnivorousFish):
    def __init__(self, name: str, gender: str) -> None:
        super().__init__(name, gender)
    
    def mate(self, other: Fish) -> Fish:
        return super().mate(other)