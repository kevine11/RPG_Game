class Character(object):
    def __init__(self, name, health, power):
        self.name = name 
        self.health = health
        self.power = power

    def Alive(self):
        return self.health > 0

class Hero(Character):

    def Attack(self,enemy):
        enemy.health -= self.power
        print(f"You do {self.power} damage to the goblin!")


    def PrintStatus(self):
        print(f"{self.name} has {self.health} health left!")

class Goblin(Character):

    def Attack(self,enemy):
        enemy.health -= self.power
        print(f"You do {self.power} damage to the hero!")
        

    def PrintStatus(self):
        print(f"{self.name} has {self.health} health left!")

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


