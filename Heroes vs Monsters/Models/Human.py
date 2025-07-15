from Models.Hero import Hero

class Human(Hero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__bonus_for = 1
        self.__bonus_end = 1

    @property
    def end(self):
        return super().end + self.__bonus_end

    @property
    def force(self):
        return super().force + self.__bonus_for

    def show_info(self):
        print("HUMAIN")
        super().show_info()