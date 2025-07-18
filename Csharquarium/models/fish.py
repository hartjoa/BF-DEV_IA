from abc import abstractmethod
from models.aquatic_organism import AquaticOrganism

class Fish(AquaticOrganism):
    def __init__(self, name, gender):
        super().__init__()
        self.name = name
        self.gender = gender
    
    @abstractmethod
    def eat(self, food):
        pass

    @abstractmethod
    def mate(self, other):
        pass