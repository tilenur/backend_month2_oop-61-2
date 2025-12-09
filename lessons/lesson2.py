# Наследование
# Родительский \Супер класс

class Hero:
    # конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибута класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} {self.lvl} "

kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 101, 1001)

# Дочерний класс
class MageHero(Hero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"{self.name} Hello! "

    def cast_spell(self):
        return f"{self.name} casted fire ball!!!"

class WarriorHero(Hero):
    def attack(self):
        return f"{self.name} attacks you with a sword!!!"

gandalf = MageHero("Gandalf", 100, 1000, 100)
aragon = WarriorHero("Aragon", 100, 1000)

# print(kirito.action())
# print(gandalf.action())
# print(aragon.action())

# print(type(gandalf))
# print(type(kirito))

# 2. Полиморфизм без наследования (duck typing)

class Car:
    def action(self):
        return "Машина едет"
class Numan:
    def action(self):
        return 'Человек идет'
class Snake:
    def action(self):
        return 'Змея ползет'

# 3. Полиморфизм через перегрузку операторов (ad-hoc polymorphism)
# print(5 + 5)
# print("5" + "5")