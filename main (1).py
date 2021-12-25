# в задании представлен один класс который нужно разбить на 4
# Воин      - Warrior
# Лекарь    - Healer
# Дерево    - Tree
# Ловушка   - Trap

# Воин в состоянии защищаться от врагов, атаковать и передвигаться по полю
# Лекарь может защищаться, лечить воина и панически спасаться бегством
# Дерево может защищаться (попробуй разруби сходу) и гореть в огне
# Ловушка не может ничего кроме как атаковать того, кто на нее наступит
# Для решения этой задачи не используйте наследование

class Warrior:

    def __init__(self):
        self.hp = 10

    def defence(self):
        pass

    def move(self):
        pass

    def attack(self):
        pass


class Healer:

    def __init__(self):
        self.hp = 20

    def defence(self):
        pass

    def heal(self, unit):
        unit.hp += 10

    def flee(self):
        pass


class Tree:

    def burn(self):
        print("I'm on fire today!")

    def defence(self):
        pass


class Trap:

    def attack(self, unit):
        print("It's a trap!")
        unit.hp -= 5


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()
    trap.attack(unit)
    healer.heal(unit)
    print(unit.hp)
