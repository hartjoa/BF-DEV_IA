from abc import ABC

class AquaticOrganism(ABC):
    def __init__(self, age: int = 0) -> None:
        self.pv = 10
        self.age = age

    @property
    def is_alive(self) -> bool:
        return self.pv > 0 and self.age <= 20