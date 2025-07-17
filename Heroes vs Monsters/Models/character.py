from abc import ABC
from Models.dice import Dice

class Character(ABC):
    def __init__(self):
        self.__endurance = Character.roll_ability(4, 3)
        self._force = Character.roll_ability(4, 3)  
        self.__pv = self.__endurance + Character.modifier(self.__endurance)
        self.__inventory = {}
    
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
    
    @staticmethod
    def roll_ability(roll_count, keep_count):
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

    # endregion

    # region properties

    @property
    def dead(self):
        return self.__pv < 1

    @property
    def force(self):
        return self._force

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, value):
        self.__endurance = value

    @property
    def pv(self):
        return self.__pv
    
    @pv.setter
    def pv(self, value):
        self.__pv = value

    @property
    def inventory(self):
        return self.__inventory

    # endregion
    
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
        self.__pv = 0
