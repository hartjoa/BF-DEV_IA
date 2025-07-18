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

    def alga_eaten(self, alga):
        alga.pv -= 2

    def elapse_time(self):
        # all algae grow
        for alga in self.algae:
            alga.pv += 1
        
        # hunger fishes eat
        for fish in self.fishes:
            fish.pv -= 1
            if fish.pv <= 5:
                # fish is hungry
                if isinstance(fish, HerbivorousFish):
                    # herbivorous
                    print(f"{fish.name} is looking for an alga to eat...")
                    if len(self.algae) == 0:
                        # no more alga in the aquarium
                        print(f"There's no more alga left to feed you, poor {fish.name}")
                        continue
                    # eat an alga
                    alga = random.choice(self.algae)
                    # alga is harmed
                    alga.pv -= 2
                    # fish is fed
                    fish.pv += 3
                elif isinstance(fish, CarnivorousFish):
                    if len(self.fishes) < 2:
                        # only fish in the aquarium
                        print(f"There's no more fish left to feed you, poor {fish.name}")
                        continue
                    # eat a fish
                    prey = None
                    while not prey or prey == fish: # cannot eat yourself
                        prey = random.choice(self.fishes)
                        if prey != fish:
                            # prey is harmed
                            prey.pv -= 4
                    # fish is fed
                    fish.pv += 5
                else:
                    raise TypeError("Any fish should be either carnivorous or herbivorous")
        
        # all the dead algae dissapear
        dead_algae = [alga for alga in self.algae if not alga.is_alive]
        for dead_alga in dead_algae:
            self.algae.remove(dead_alga)
        
        # all the dead fishes dissapear
        dead_fishes = [fish for fish in self.fishes if not fish.is_alive]
        for dead_fish in dead_fishes:
            self.fishes.remove(dead_fish)
