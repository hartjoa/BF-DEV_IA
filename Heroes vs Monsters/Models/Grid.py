import random
from Models.Hero import Hero
from rich.table import Table
from rich.console import Console
from rich.live import Live
import time
import msvcrt

class Grid():
    def __init__(self, size):
        self.__size = size
        self.__grid = []  # 2D data
        self.__table = None
        self.initialize()

    def initialize(self):
        for _ in range(self.__size):
            row_squares = []
            for _ in range(self.__size):
                row_squares.append(None)
            self.__grid.append(row_squares)
        self.__table = self.build()

    def add_character(self, character):
        x = character.x
        y = character.y
        if (
            x >= self.__size or 
            y >= self.__size or 
            x < 0 or 
            y < 0
            ):
            raise IndexError(f"Taille de la grille: {self.__size} x {self.__size}")
        if not self.is_empty_square(x, y):
            raise IndexError(f"Il y a déjà un personnage ({self.character_on_square(x, y)}) sur la case ({x}, {y})")

        self.__grid[x][y] = character
        self.__table = self.build()
        
    def move_character(self, character, new_x, new_y):
        old_x, old_y = character.x, character.y
        character.x, character.y = new_x, new_y
        try:
            self.add_character(character)
        except IndexError:
            character.x, character.y = old_x, old_y
            return False
        else:
            self.__grid[old_x][old_y] = None
        self.__table = self.build()
        return True
        
    def character_on_square(self, x, y):
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
    
    def on_press(self, key, live):
        if key.name == "esc":
            self.stop = True
            return False
        
        self.move_hero(key.name)

    def move_hero(self, live, direction):
        hero = self.find_hero()
        x, y = hero.x, hero.y
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
            live.update(self.build())
    
    def play(self):
        stop = False
        print("ok c'est go")
        with Live(self.build(), refresh_per_second=4) as live:
            while not stop:
                key = msvcrt.getch()
                if key == b'\xe0':    # special key
                    direction = msvcrt.getch()  
                    self.move_hero(live, direction)
                elif key == b'\x1b':
                    stop = True
    
    def is_empty_square(self, x, y):
        return not self.__grid[x][y]
    
    def build(self):
        table = Table(show_header=False, show_lines=True)
        for _ in range(self.__size):
            table.add_column(justify="center")
        for row in self.__grid:
            table.add_row(*[" " if not cell 
                            else f"[bold]{str(cell)}" if isinstance(cell, Hero) 
                            else str(cell) for cell in row])
        return table
    
    def get_random_empty_square(self):
        while True:
            x = random.randint(0, self.__size - 1)
            y = random.randint(0, self.__size - 1)
            if self.is_empty_square(x, y):
                return (x, y)