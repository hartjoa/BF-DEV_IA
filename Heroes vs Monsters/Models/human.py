from Models.hero import Hero

class Human(Hero):
    def __init__(self):
        super().__init__()
        self.__bonus_for = 1
        self.__bonus_endurance = 1

    @property
    def endurance(self):
        return super().endurance + self.__bonus_endurance

    @property
    def force(self):
        return super().force + self.__bonus_for

    def show_info(self):
        print("HUMAIN")
        super().show_info()
    
    def __str__(self):
        return "💀" if self.dead else "🧞"
