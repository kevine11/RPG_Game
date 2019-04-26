class Character(object):
    def __init__(self, name, health, power):
        self.name = name 
        self.health = health
        self.power = power

    def Alive(self):
        return self.health > 0

    def Attack(self,enemy):
        enemy.health -= self.power
        print(f"The {self.name} has done {self.power} damage to the {enemy.name}")

    def PrintStatus(self):
        print(f"{self.name} has {self.health} health left!")

class Hero(Character):
    pass
    

class Goblin(Character):
    pass


hero = Hero('Hero',10, 5)
goblin = Goblin('Goblin',6,2)

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


