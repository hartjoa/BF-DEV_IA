from Models.human import Human
from Models.dwarf import Dwarf
from Models.wolf import Wolf
from Models.wyrmling import Wyrmling
from Models.orc import Orc
from Models.grid import Grid
import random
from os import system
import constants as k
# Create playground
playground = Grid(k.GRID_SIZE)

# Create a hero
x, y = playground.get_random_empty_square()
hero_race = random.choice(k.HEROES)
hero = None
match hero_race:
    case 'Human':
        hero = Human()
    case 'Dwarf':
        hero = Dwarf()
    case _:
        raise ValueError(f"La race de héros '{hero_race}' n'est pas définie")
# Add hero to playground
playground.add_character(hero, x, y)

# Create monsters
for i in range(k.MONSTERS_COUNT):
    x, y = playground.get_random_empty_square()
    monster_race = random.choice(k.MONSTERS)
    monster = None
    match monster_race:
        case 'Wolf':
            monster = Wolf()
        case 'Wyrmling':
            monster = Wyrmling()
        case 'Orc':
            monster = Orc()
        case _:
            raise ValueError(f"La race de monstre '{monster_race}' n'est pas définie")
    # Add monster to playground
    monster.visible = False
    playground.add_character(monster, x, y)

system("cls")
playground.play()