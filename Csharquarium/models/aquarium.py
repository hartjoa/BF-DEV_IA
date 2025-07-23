from models.alga import Alga
from models.fish import Fish
from models.herbivorous_fish import HerbivorousFish
from models.carnivorous_fish import CarnivorousFish
from models.log import Log
from utils import Utils

from typing import List
from colorama import Fore
import random

class Aquarium:
    def __init__(self, fishes: List[Fish] = None, algae: List[Alga] = None) -> None:
        self.algae = algae if algae is not None else []
        self.fishes = fishes if fishes is not None else []
    
    def add_fish(self, fish: Fish) -> None:
        if isinstance(fish, Fish) and fish.is_alive:
            self.fishes.append(fish)

    def add_alga(self, alga: Alga) -> None:
        if isinstance(alga, Alga):
            self.algae.append(alga)
    
    def describe(self) -> None:
        Utils.nice_print(f"Algae in the aquarium: {len(self.algae)}", Fore.GREEN)
        for alga in self.algae:
            print(alga)
        Utils.nice_print(f"Fishes in the aquarium: {len(self.fishes)}", Fore.BLUE)
        print("\n".join([str(fish) for fish in self.fishes]))

    def alga_eaten(self, alga: Alga) -> None:
        alga.pv -= 2

    def run_lifecycle(self) -> None:
        log = Log("./log.log")

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
                    alga = fish.find_alga(self)
                    if not alga:
                        continue

                    fish.eat(alga)
                elif isinstance(fish, CarnivorousFish):
                    # carnivorous
                    prey = fish.find_prey(self)
                    if not prey:
                        continue

                    fish.eat(prey)
                else:
                    raise TypeError("Any fish should be either carnivorous or herbivorous")
            else:
                # mate
                partner = random.choice([other_fish for other_fish in self.fishes if other_fish != fish])
                baby_fish = fish.mate(partner)
                if baby_fish:
                    self.add_fish(baby_fish)
        
        # big algae split
        for alga in self.algae:
            if alga.pv >= 10:
                new_alga = alga.split()
                self.add_alga(new_alga)

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
        
        
