import random
from Models.Hero import Hero
from Models.Monster import Monster

class Grid():
    def __init__(self, size):
        self.__size = size
        self.__grid = []
        self.initialize()

    def initialize(self):
        for row in range(self.__size):
            row_squares = []
            for col in range(self.__size):
                row_squares.append(None)
            self.__grid.append(row_squares)

    def add_character(self, character):
        x = character.x
        y = character.y
        if x >= self.__size or y >= self.__size:
            raise IndexError(f"Taille de la grille: {self.__size} x {self.__size}")
        if not self.is_empty_square(x, y):
            raise IndexError(f"Il y a déjà un personnage ({self.character_on_square(x, y)}) sur la case ({x}, {y})")

        self.__grid[x][y] = character
        
    def character_on_square(self, x, y):
        return self.__grid[x][y]

    def show(self):
        for row in range(self.__size):
            row_str = ""
            for col in range(self.__size):
                character = self.__grid[row][col]
                must_show = (
                    character and (
                        isinstance(character, Hero) or
                        (isinstance(character, Monster) and character.visible)
                    )
                )
                row_str += "*" if not must_show else str(character)
            print(row_str)
    
    def is_empty_square(self, x, y):
        return not self.__grid[x][y]
    
    def get_random_empty_square(self):
        while True:
            x = random.randint(0, self.__size - 1)
            y = random.randint(0, self.__size - 1)
            if self.is_empty_square(x, y):
                return (x, y)