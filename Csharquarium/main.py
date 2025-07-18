from models.aquarium import Aquarium
from models.alga import Alga
from models.herbivorous_fish import HerbivorousFish
from models.clownfish import Clownfish
from models.grouper import Grouper
from models.tuna import Tuna
from models.sole import Sole
from models.sea_bass import SeaBass
from models.carp import Carp
import os

os.system("cls" if os.name == "nt" else "clear")

my_aquarium = Aquarium()
alga1 = Alga()
alga2 = Alga()
alga3 = Alga()
my_aquarium.add_alga(alga1)
my_aquarium.add_alga(alga2)
my_aquarium.add_alga(alga3)

maurice = Sole("Maurice", "Male")
dory = Clownfish("Dory", "Female")
percy = Clownfish("Percy", "Male")
aglae = Tuna("Aglaë", "Female")
ston = Grouper("Ston", "Male")
muut = Carp("Muût", "Female")
open = SeaBass("Open", "Female")
johnson = Sole("Johnson", "Male")

my_aquarium.add_fish(maurice)
my_aquarium.add_fish(dory)
my_aquarium.add_fish(percy)
my_aquarium.add_fish(aglae)
my_aquarium.add_fish(ston)
my_aquarium.add_fish(muut)
my_aquarium.add_fish(open)
my_aquarium.add_fish(johnson)

day = 1
my_aquarium.describe()
for _ in range(100):
    print(f"\n === Day {day} ===")
    my_aquarium.elapse_time()
    day += 1
    my_aquarium.describe()
