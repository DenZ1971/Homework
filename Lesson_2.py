from random import randint


class Character:

    def __init__(self, life, armor, impact_force):
        self.life = life
        self.armor = armor
        self.impact_force = impact_force

    def attack(self):
        att = randint(*self.impact_force)
        return att

    def damage(self, att):
        if att > self.armor:
            self.life = self.life - att
            if self.life > 0:
                return f"Остаток жизни - {self.life}"
            else:
                return f"Погиб"
        else:
            return f"Броня не пробита"



c = Character(10, 6, (5, 10))
d = Character(10, 6, (5, 10))



def game(F1, F2):
    while True:
        a1 = F1.attack()
        print(f"Игрок 1 наносит удар силой {a1}")
        d2 = F2.damage(a1)
        print(f"Игрок 2: {d2}")
        if d2 == "Погиб":
            break
        a2 = F2.attack()
        print(f"Игрок 2 наносит удар силой {a2}")
        d1 = F1.damage(a1)
        print(f"Игрок 1: {d1}")
        if d1 == "Погиб":
            break




game(c, d)