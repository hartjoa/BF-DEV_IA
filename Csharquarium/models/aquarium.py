from models.alga import Alga
from models.fish import Fish
from models.herbivorous_fish import HerbivorousFish
from models.carnivorous_fish import CarnivorousFish
import random 

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
    
    def describe(self):
        print("Algae in the aquarium:", len(self.algae))
        print("Fishes in the aquarium:", len(self.fishes))
        print()
        print("\n".join([str(fish) for fish in self.fishes]))

    def elapse_time(self):
        # all the fishes eat
        for fish in self.fishes:
            food = None
            if isinstance(fish, HerbivorousFish):
                if len(self.algae) < 1:
                    print(f"There's no more alga left to feed you, poor {fish.name}")
                    continue
                food = random.choice(self.algae)
                self.algae.remove(food)
            elif isinstance(fish, CarnivorousFish):
                if len(self.fishes) < 2:
                    print(f"There's no more fish left to feed you, poor {fish.name}")
                    break
                while not food or food == fish: # cannot eat yourself
                    food = random.choice(self.fishes)
                    if food != fish:
                        self.fishes.remove(food)
            else:
                raise TypeError("Any fish should be either carnivorous or herbivorous")
