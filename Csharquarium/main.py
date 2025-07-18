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
maurice.age = 7
dory = Clownfish("Dory", "Female")
percy = Clownfish("Percy", "Male")
aglae = Tuna("Aglae", "Female")
aglae.age = 16
ston = Grouper("Ston", "Male")
muut = Carp("Muût", "Female")
oriana = SeaBass("Oriana", "Female")
oriana.age = 22
johnson = Sole("Johnson", "Male")

my_aquarium.add_fish(maurice)
my_aquarium.add_fish(dory)
my_aquarium.add_fish(percy)
my_aquarium.add_fish(aglae)
my_aquarium.add_fish(ston)
my_aquarium.add_fish(muut)
my_aquarium.add_fish(oriana)
my_aquarium.add_fish(johnson)

day = 1
my_aquarium.describe()
for _ in range(30):
    print(f"\n === Day {day} ===")
    my_aquarium.elapse_time()
    day += 1
    my_aquarium.describe()
