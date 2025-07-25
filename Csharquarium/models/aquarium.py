from .alga import Alga
from .fish import Fish
from .herbivorous_fish import HerbivorousFish
from .carnivorous_fish import CarnivorousFish
from .log import Log
from utils import Utils

from typing import List
from colorama import Fore
import random

class Aquarium:
    def __init__(self, fishes: List[Fish] = None, algae: List[Alga] = None) -> None:
        self.algae = algae if algae is not None else []
        self.fishes = fishes if fishes is not None else []
        self.age = 0
    
    def add_fish(self, fish: Fish) -> None:
        if isinstance(fish, Fish) and fish.is_alive:
            self.fishes.append(fish)

    def add_alga(self, alga: Alga) -> None:
        if isinstance(alga, Alga):
            self.algae.append(alga)
    
    def description(self) -> List[str]:
        result = ["=== Day ==="]
        result.append(str(self.age))
        result.append(f"=== Algae ({len(self.algae)}) ===")
        algae_by_age = {}
        for alga in self.algae:
            if alga.age in algae_by_age:
                algae_by_age[alga.age] += 1
            else:
                algae_by_age[alga.age] = 1
        for age, count in sorted(algae_by_age.items()):
            result.append(f"{count} alga(e) - {age} days")
        result.append(f"=== Fishes ({len(self.fishes)}) ===")
        result.extend([str(fish) for fish in self.fishes])
        return result
    
    def save_state(self, file_path = "data.aquarium"):
        try:
            with open(file_path, "w") as file:
                file.write(self.describe)
        except Exception as e:
            print(f"Could not write in file '{file_path}': {e}")


    def run_lifecycle(self, verbose: bool = False) -> None:
        # everybody gets older
        for fish in self.fishes:
            fish.age += 1
        for alga in self.algae:
            alga.age +=1

        # all algae grow
        for alga in self.algae:
            alga.pv += 1
                    
        # all fishes get hungrier
        for fish in self.fishes:
            fish.pv -= 1

            # eat or mate
            if fish.pv <= 5:
                # eat
                if isinstance(fish, HerbivorousFish):
                    # herbivorous
                    alga = fish.find_alga(self, verbose)
                    if not alga:
                        continue

                    fish.eat(alga, verbose)
                elif isinstance(fish, CarnivorousFish):
                    # carnivorous
                    prey = fish.find_prey(self, verbose)
                    if not prey:
                        continue

                    fish.eat(prey, verbose)
                else:
                    raise TypeError("Any fish should be either carnivorous or herbivorous")
            else:
                # mate
                partner = random.choice([other_fish for other_fish in self.fishes if other_fish != fish])
                baby_fish = fish.mate(partner, verbose)
                if baby_fish:
                    self.add_fish(baby_fish)
        
        # big algae split
        for alga in self.algae:
            if alga.pv >= 10:
                new_alga = alga.split()
                self.add_alga(new_alga)

        # all the dead algae dissapear
        dead_algae = [alga for alga in self.algae if not alga.is_alive]
        Utils.nice_print(f"{len(dead_algae)} algae died...", Fore.RED)
        for dead_alga in dead_algae:
            self.algae.remove(dead_alga)
        
        # all the dead fishes dissapear
        dead_fishes = [fish for fish in self.fishes if not fish.is_alive]
        for dead_fish in dead_fishes:
            Utils.nice_print(f"A fish died... RIP {dead_fish.name}", Fore.RED)
            self.fishes.remove(dead_fish)

        # aquarium gets older
        self.age += 1        
        
