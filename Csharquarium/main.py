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
species = [Sole, ]
for _ in range(10):
    sole = Fish.generate(Sole)
    my_aquarium.add_fish(sole)

alga1 = Alga()
alga2 = Alga()
alga3 = Alga()
my_aquarium.add_alga(alga1)
my_aquarium.add_alga(alga2)
my_aquarium.add_alga(alga3)

maurice = Sole("Maurice", "Male")
maurice.age = 7
dory = Clownfish("Dory", "Female")
percy = Tuna("Percy", "Male")
aglae = Sole("Aglae", "Female")
aglae.age = 16
ston = Carp("Ston", "Male")
muut = Clownfish("Muût", "Male")
oriana = Tuna("Oriana", "Female")
oriana.age = 22
johnson = Carp("Johnson", "Female")

my_aquarium.add_fish(maurice)
my_aquarium.add_fish(dory)
my_aquarium.add_fish(percy)
my_aquarium.add_fish(aglae)
my_aquarium.add_fish(ston)
my_aquarium.add_fish(muut)
my_aquarium.add_fish(oriana)
my_aquarium.add_fish(johnson)

day = 1

while True:
    _ = input()
    Utils.nice_print(f"=== DAY {day} ===", Fore.YELLOW)
    print()
    my_aquarium.run_lifecycle()
    my_aquarium.describe()
    day +=1
    