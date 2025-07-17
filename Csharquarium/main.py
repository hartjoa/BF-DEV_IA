from models.aquarium import Aquarium
from models.alga import Alga
from models.herbivorous_fish import HerbivorousFish
from models.carnivorous_fish import CarnivorousFish

my_aquarium = Aquarium()
my_aquarium.add_alga(Alga())
my_aquarium.add_alga(Alga())
my_aquarium.add_alga(Alga())
my_aquarium.add_fish(HerbivorousFish("Maurice", "Male"))
my_aquarium.add_fish(CarnivorousFish("Dory", "Female"))

my_aquarium.elapse_time()