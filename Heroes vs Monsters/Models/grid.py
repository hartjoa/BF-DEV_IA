import random
from Models.hero import Hero
from Models.monster import Monster
from Models.fight import Fight
from rich.table import Table
from rich.console import Console
from rich.live import Live
import msvcrt

class Grid():
    def __init__(self, size):
        self.__size = size
        self.__grid = []
        self.__table = None
        self.__console_message = ""
        self.__monsters_count = 0
        self.initialize()

    def initialize(self):
        for _ in range(self.__size):
            row_squares = []
            for _ in range(self.__size):
                row_squares.append(None)
            self.__grid.append(row_squares)
        self.__table = self.build()

    def get_character_position(self, character):
        for x, row in enumerate(self.__grid):
            for y, cell in enumerate(row):
                if cell == character:
                    return (x, y)
        return(None, None)

    def add_character(self, character, x, y):
        if (
            x >= self.__size or 
            y >= self.__size or 
            x < 0 or 
            y < 0
            ):
            raise IndexError(f"Taille de la grille: {self.__size} x {self.__size}")
        if not self.is_empty_square(x, y):
            raise IndexError(f"Il y a déjà un personnage ({self.get_character(x, y)}) sur la case ({x}, {y})")

        self.__grid[x][y] = character
        self.__table = self.build()
        if isinstance(character, Monster):
            self.__monsters_count += 1
        
    def move_character(self, character, new_x, new_y):
        old_x, old_y = self.get_character_position(character)
        try:
            self.add_character(character, new_x, new_y)
        except IndexError:
            character.x, character.y = old_x, old_y
            return False
        else:
            self.__grid[old_x][old_y] = None
        self.__table = self.build()
        return True
        
    def get_character(self, x, y):
        return self.__grid[x][y]

    def show(self):
        console = Console()
        console.print(self.__table)
    
    def find_hero(self):
        for row in self.__grid:
            for cell in row:
                if isinstance(cell, Hero):
                    return cell
        return None
    
    def move_hero(self, direction):
        hero = self.find_hero()
        x, y  = self.get_character_position(hero)
        match direction:
            case b'H':
                x -= 1
            case b'P':
                x += 1
            case b'K':
                y -= 1
            case b'M':
                y += 1
        if self.move_character(hero, x, y):
            return (x, y)
        else:
            return (None, None)
            
    def play(self):
        stop = False
        print("ok c'est go")
        with Live(self.build(), refresh_per_second=4) as live:
            while not stop:
                key = msvcrt.getch()
                if key == b'\xe0':    # special key
                    direction = msvcrt.getch()  
                    x, y = self.move_hero(direction)
                    if (x, y) == (None, None):
                        continue

                    live.update(self.build())
                    self.__console_message = ""
                    hero = self.get_character(x, y)
                    for monster in self.monsters_around(x, y):
                        monster.visible = True
                        self.__console_message = f"\nLe monstre {monster} vient d'apparaître\nPressez une touche pour lancer le combat...\n"
                        self.__monsters_count -= 1
                        live.update(self.build())
                        msvcrt.getwch()
                        fight = Fight(hero, monster)
                        log = fight.run()
                        self.__console_message += "\n".join(log)
                        if hero.dead:
                            self.__console_message += "\n^^^^^Game Over^^^^^\nPressez une touche pour terminer"
                            hero.pv = 0
                            live.update(self.build())
                            msvcrt.getwch()
                            stop = True
                            break
                        elif monster.dead:
                            self.__console_message += "\nLe héros a tué le monstre!\nPressez une touche pour poursuivre..."
                            monster.pv = 0
                            monster.give_resources(hero)
                            live.update(self.build())
                            msvcrt.getwch()
                            self.__console_message = ""
                            dead_x, dead_y = self.get_character_position(monster)
                            self.__grid[dead_x][dead_y] = None
                            live.update(self.build())
                elif key == b'\x1b':
                    stop = True
    
    def is_empty_square(self, x, y):
        return not self.__grid[x][y]
    
    def monsters_around(self, x, y):
        result = []
        min_x = x - 1 if x > 0 else x
        max_x = x + 1 if x < self.__size - 1 else x
        min_y = y - 1 if y > 0 else y
        max_y = y + 1 if y < self.__size - 1 else y
        for row in range(min_x, max_x + 1):
            for col in range(min_y, max_y + 1):
                if isinstance(self.__grid[row][col], Monster):
                    result.append(self.__grid[row][col])
        return result
        
    def display_cell(cell):
        if not(cell):
            return "  " 
        if isinstance(cell, Hero):
            if cell.dead:
                return f"{str(cell)}"
            return f"{str(cell)}"
        if cell.visible:
            if cell.dead:
                return f"{str(cell)}"
            return f"{str(cell)}"
        return " "
    
    def build(self):
        main_table = Table(show_header=False)
        main_table.add_column(justify="center")
        main_table.add_column(justify="center")
        playground_table = Table(show_header=False, show_lines=True)
        for _ in range(self.__size):
            playground_table.add_column(justify="center")
        for row in self.__grid:
            playground_table.add_row(*[Grid.display_cell(cell) for cell in row])
        main_table.add_row(playground_table, self.__console_message)
        hero = self.find_hero()
        gold = "-" if not hero or "Gold" not in hero.inventory else str(hero.inventory["Gold"])
        leather = "-" if not hero or "Leather" not in hero.inventory else str(hero.inventory["Leather"])
        main_table.add_row(f"Monstres encore cachés dans la forêt: {self.__monsters_count}", f"Or: {gold}\nCuir: {leather}")
        return main_table
    
    def get_random_empty_square(self):
        while True:
            x = random.randint(0, self.__size - 1)
            y = random.randint(0, self.__size - 1)
            if self.is_empty_square(x, y):
                return (x, y)
