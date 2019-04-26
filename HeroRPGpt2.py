import random

class Character(object):
    def __init__(self, name, health, power, armor):
        self.name = name 
        self.health = health
        self.power = power
        self.armor = armor

    def Alive(self):
        return self.health > 0

    def Attack(self,enemy):
        roll = rand.int(1,20)
        if self.roll > enemy.roll:
            enemy.health -= self.power * 2
            print(f"The {self.name} has done {self.power} CRITICAL damage to the {enemy.name}!")
        if self.roll < enemy.roll:
            print(f"The {self.name} has done {self.power} damage to the {enemy.name}")

    def PrintStatus(self):
        print(f"{self.name} has {self.health} health left!")

class Hero(Character):
    pass

class Medic(Character):
    pass

class Shadow(Character):
    pass

class Goblin(Character):
    pass

class Zombie(Character):
    pass

class GunSlinger(Character):
    pass

class OverLord(Character):
    pass

class DarkKnight(Character):
    pass


darkknight = DarkKnight('Dark Knight', 50, 6, 12)
gunslinger = GunSlinger('Gun Slinger', 23, 8, 7)
zombie = Zombie('White Walker', 0, 1, 0)
medic = Medic('Medic', 30, 4, 5)
shadow = Shadow('Shadow',1 ,9, 4)
hero = Hero('Hero',20, 10, 10)
goblin = Goblin('Goblin', 12, 4, 3)

while goblin.health and hero.health > 0:
    hero.PrintStatus()
    goblin.PrintStatus()
    print(f"The goblin has {goblin.health} health and {goblin.power} power.")
    print("What do you want to do?")
    print("1. Fight Goblin")
    print("2. Do Nothing")
    print("3. Flee")
    print("> ", end=' ')

    raw_input = input()

    if raw_input == "1":
        hero.Attack(goblin)
        if goblin.health <= 0:
            print("You have slain your enemy!")
            break

    elif raw_input == "2":
        goblin.Attack(hero)
        if hero.health <= 0:
            print("You have fallen to a Goblin!")
            break


    elif raw_input == "3":
        print("You ran like a coward!")
        break

    else:
        print("Invalid input {}".format(raw_input))


