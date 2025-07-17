from abc import ABC
from Models.dice import Dice

class Character(ABC):
    def __init__(self, x, y):
        self.__endurance = Character.ability(4, 3)  # Endurance
        self._force = Character.ability(4, 3)  # Force
        self.__pv = self.__endurance + Character.modifier(self.__endurance)  # Points de vie (PV)
        self.__dead = False
        self.__leather = 0  # Cuir
        self.__gold = 0     # Or
        self.__x = x        # Position X
        self.__y = y        # Position Y
    
    # region Static Methods

    @staticmethod
    def modifier(score):
        """
        Takes a characteristic's score and returns the modifier that has to be added to it_

        Args:
            score (int): The characteristic's score used to compute the modifier
        """
        if score < 5:
            return -1
        if score < 10:
            return 0
        if score < 15:
            return 1
        return 2

    # endregion

    @property
    def dead(self):
        return self.__dead

    @dead.setter
    def dead(self, value):
        self.__dead = value

    @property
    def force(self):
        return self._force

    @property
    def end(self):
        return self.__endurance

    @property
    def pv(self):
        return self.__pv
    
    @property
    def gold(self):
        return self.__gold

    @gold.setter
    def gold(self, value):
        self.__gold = value

    @property
    def leather(self):
        return self.__leather

    @leather.setter
    def leather(self, value):
        self.__leather = value
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

    @staticmethod
    def ability(roll_count, keep_count):
        """
        Utility method that rolls dice and returns the sum of the best dice
        Args:
            roll_count (int): the amount of dice to roll
            keep_count (int): the amount of best dice to keep to make the sum
        """
        if keep_count > roll_count:
            raise ValueError("Impossible to keep more dice than those who were rolled...")

        dice_results = []
        # Roll [roll_count] dice
        for i in range(roll_count):
            dice_results.append(Dice(1, 6).roll())
        # Sort the outcome
        dice_results.sort(reverse = True)
        # Make the sum
        return sum(dice_results[0:keep_count])
    
    

    def hit(self):
        return Dice(1, 4).roll() + Character.modifier(self._force)

    def show_info(self):
        print(f"[{self.x} x {self.y}]")
        print(20 * '=')
        print("Endurance:",self.end)
        print("Force:",self.force)
        print("PV:",self.__pv)
        print("En vie?", not self.dead)
        print("Cuir:",self.leather)
        print("Or:",self.__gold)
        print(20 * '=' + "\n")
    
    def die(self):
        self.__dead = True
        self.__pv = 0
