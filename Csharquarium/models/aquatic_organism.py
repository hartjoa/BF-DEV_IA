from abc import ABC

class AquaticOrganism(ABC):
    def __init__(self):
        self.pv = 10
        self.age = 0

    @property
    def is_alive(self):
        return self.pv > 0 and self.age <= 20