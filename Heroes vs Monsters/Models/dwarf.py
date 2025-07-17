from Models.hero import Hero

class Dwarf(Hero):
    def __init__(self):
        super().__init__()
        self.__bonus_endurance = 2

    @property
    def endurance(self):
        return super().endurance + self.__bonus_endurance

    def show_info(self):
        print("NAIN")
        super().show_info()
    
    def __str__(self):
        return "😶‍🌫️"
