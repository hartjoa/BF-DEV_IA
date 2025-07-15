from Models.Hero import Hero

class Dwarf(Hero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__bonus_end = 2

    @property
    def end(self):
        return super().end + self.__bonus_end

    def show_info(self):
        print("NAIN")
        super().show_info()
