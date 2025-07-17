from abc import ABC, abstractmethod

class Fish(ABC):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    @abstractmethod
    def eat(food):
        pass