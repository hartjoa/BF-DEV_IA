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

alga1 = Alga()
alga2 = Alga()
alga3 = Alga()
my_aquarium.add_alga(alga1)
my_aquarium.add_alga(alga2)
my_aquarium.add_alga(alga3)

day = 1

while True:
    _ = input()
    Utils.nice_print(f"=== DAY {day} ===", Fore.YELLOW)
    print()
    my_aquarium.run_lifecycle()
    my_aquarium.describe()
    day +=1
    