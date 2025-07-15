from Models.Hero import Hero
from Models.Monster import Monster

class Fight():
    def __init__(self, hero, monster):
        if not isinstance(hero, Hero):
            raise TypeError("Only a hero can start a fight")
        if not isinstance(monster, Monster):
            raise TypeError("A hero can only fight a monster")
        self.__hero = hero
        self.__monster = monster
    
    def run(self):
        hero_pv = self.__hero.pv
        monster_pv = self.__monster.pv
        print(f"Le combat va opposer un héros ({hero_pv}) à un monstre ({monster_pv})")
        while hero_pv > 0 and monster_pv > 0:
            # Hero attacks
            damage = self.__hero.hit()
            monster_pv -= damage
            print(f"Attaque du héros: {damage}. PV du monstre: {monster_pv}")
            if monster_pv > 0:
                # Monster attacks
                damage = self.__monster.hit()
                hero_pv -= damage
                print(f"Attaque du monstre: {damage}. PV du héros: {hero_pv}")
        if hero_pv < 1:
            self.__hero.die()
        if monster_pv < 1:
            self.__monster.die()
