from models.alga import Alga
from models.fish import Fish

class Aquarium:
    def __init__(self, fishes = [], algae = []):
        self.algae = algae
        self.fishes = fishes
    
    def add_fish(self, fish):
        if isinstance(fish, Fish):
            self.fishes.append(fish)

    def add_alga(self, alga):
        if isinstance(alga, Alga):
            self.algae.append(alga)

    def elapse_time(self):
        print("Algae in the aquarium:", len(self.algae))
        print("Fishes in the aquarium:", len(self.fishes))
        print("\n".join([f"{fish.name} ({fish.gender[0].upper()})" for fish in self.fishes]))