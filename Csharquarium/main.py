from models.aquarium import Aquarium
from models.alga import Alga
from models.herbivorous_fish import HerbivorousFish
from models.clownfish import Clownfish
from models.grouper import Grouper
from models.tuna import Tuna
from models.sole import Sole
from models.sea_bass import SeaBass
from models.carp import Carp
from models.fish import Fish
from utils import Utils

import os
import random
from colorama import Fore

os.system("cls" if os.name == "nt" else "clear")

my_aquarium = Aquarium()

# add fishes
species = [Carp, Clownfish, Grouper, SeaBass, Sole, Tuna]
for sp in species:
    for _ in range(10):
        fish = Fish.generate(sp)
        my_aquarium.add_fish(fish)

# add algae
for _ in range(15):
    my_aquarium.add_alga(Alga())

day = 1

# run simulation
for day in range(10):
    Utils.nice_print(f"\n=== DAY {day + 1} ===", Fore.YELLOW)
    my_aquarium.run_lifecycle(verbose=False)
    my_aquarium.description(verbose=False)
    