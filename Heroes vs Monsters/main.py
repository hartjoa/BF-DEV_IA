from Models.Human import Human
from Models.Monster import Monster
from Models.Dwarf import Dwarf
from Models.Wolf import Wolf
from Models.Wyrmling import Wyrmling
from Models.Orc import Orc
from Models.Grid import Grid
from Models.Fight import Fight
import random

GRID_SIZE = 15
MONSTERS_COUNT = 10

MONSTERS = ['Wolf', 'Wyrmling', 'Orc']
HEROES = ['Human', 'Dwarf']

# Create playground
playground = Grid(GRID_SIZE)

# Create a hero
x, y = playground.get_random_empty_square()
hero_race = random.choice(HEROES)
hero = None
match hero_race:
    case 'Human':
        hero = Human(x, y)
    case 'Dwarf':
        hero = Dwarf(x, y)
    case _:
        raise ValueError(f"La race de héros '{hero_race}' n'est pas définie")
# Add hero to playground
playground.add_character(hero)

# Create monsters
for i in range(MONSTERS_COUNT):
    x, y = playground.get_random_empty_square()
    monster_race = random.choice(MONSTERS)
    monster = None
    match monster_race:
        case 'Wolf':
            monster = Wolf(x, y)
        case 'Wyrmling':
            monster = Wyrmling(x, y)
        case 'Orc':
            monster = Orc(x, y)
        case _:
            raise ValueError(f"La race de monstre '{monster_race}' n'est pas définie")
    # Add monster to playground
    playground.add_character(monster)

playground.show()

while not