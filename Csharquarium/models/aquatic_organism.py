from abc import ABC

class AquaticOrganism(ABC):
    def __init__(self):
        self.pv = 10

    @property
    def is_alive(self):
        return self.pv > 0