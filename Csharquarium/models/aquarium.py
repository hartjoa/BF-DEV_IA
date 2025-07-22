from models.alga import Alga
from models.fish import Fish
from models.herbivorous_fish import HerbivorousFish
from models.carnivorous_fish import CarnivorousFish
from models.log import Log
from utils import Utils

import random
from colorama import Fore

class Aquarium:
    def __init__(self, fishes = [], algae = []):
        self.algae = algae
        self.fishes = fishes
    
    def add_fish(self, fish):
        if isinstance(fish, Fish) and fish.is_alive:
            self.fishes.append(fish)

    def add_alga(self, alga):
        if isinstance(alga, Alga):
            self.algae.append(alga)
    
    def describe(self):
        Utils.nice_print(f"Algae in the aquarium: {len(self.algae)}", Fore.GREEN)
        for alga in self.algae:
            print(alga)
        Utils.nice_print(f"Fishes in the aquarium: {len(self.fishes)}", Fore.BLUE)
        print("\n".join([str(fish) for fish in self.fishes]))

    def alga_eaten(self, alga):
        alga.pv -= 2

    def run_lifecycle(self):
        log = Log("./log.log")

        # everybody gets older
        for fish in self.fishes:
            fish.age += 1

        # all algae grow
        for alga in self.algae:
            alga.pv += 1
                    
        # all fishes get hungrier
        for fish in self.fishes:
            fish.pv -= 1

            # hunger fishes eat
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
                    print(f"Alga loses 2 pv => {alga.pv}")
                    # fish is fed
                    fish.pv += 3
                    print(f"Delicious! {fish.name} won 3pv => {fish.pv}")
                elif isinstance(fish, CarnivorousFish):
                    print(f"{fish.name} is looking for a fish to eat...")
                    if len(self.fishes) < 2:
                        # only fish in the aquarium
                        print(f"There's no more fish left to feed you, poor {fish.name}")
                        continue
                    # eat a fish
                    prey = random.choice(self.fishes)
                    if type(prey) == type(fish):
                        # cannot eat a fish like you
                        print(f"Sorry {fish.name}, cannot eat a fish like you")
                    else:
                        # prey is harmed
                        prey.pv -= 4
                        print(f"{prey.name} loses 4 pv => {prey.pv}")
                        # fish is fed
                        fish.pv += 5
                        print(f"Delicious! I loved you, {prey.name}... {fish.name} won 5pv => {fish.pv}")
                else:
                    raise TypeError("Any fish should be either carnivorous or herbivorous")
            else:
                # not hunger fishes try to mate
                partner = random.choice([other_fish for other_fish in self.fishes if other_fish != fish])
                baby_fish = fish.mate(partner)
                if baby_fish:
                    self.add_fish(baby_fish)
        
        # all the dead algae dissapear
        dead_algae = [alga for alga in self.algae if not alga.is_alive]
        for dead_alga in dead_algae:
            print("An alga died...")
            self.algae.remove(dead_alga)
        
        # all the dead fishes dissapear
        dead_fishes = [fish for fish in self.fishes if not fish.is_alive]
        for dead_fish in dead_fishes:
            Utils.nice_print(f"A fish died... RIP {dead_fish.name}", Fore.RED)
            self.fishes.remove(dead_fish)
        
        for alga in self.algae:
            alga.age +=1
