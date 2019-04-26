class Hero:
    def __init__(self, hero, health, power):
        self.hero = hero
        self.health = health
        self.power = power

    def Attack(self,enemy):
        enemy.health -= self.power
        print(f"You do {self.power} damage to the goblin.")
        if enemy.health <= 0:
            print("The goblin is dead.")

    def Alive(self):
        return self.health > 0

    def PrintStatus(self):
        print(f"{self.hero} has {self.health} health left")

class Goblin:
    def __init__(self, goblin, health, power):
        self.goblin = goblin
        self.health = health
        self.power = power

    def Attack(self,enemy):
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if enemy.health <= 0:
            print("You are dead.")

    def Alive(self):
        return self.health > 0

    def PrintStatus(self):
        print(f"{self.goblin} has {self.health} health left")

hero = Hero('Hero',10, 5)
goblin = Goblin('Goblin',6,2)

while goblin.health and hero.health > 0:
    hero.PrintStatus()
    goblin.PrintStatus()
    print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
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

    elif raw_input == "2":
        goblin.Attack(hero)
        if hero.health <= 0:
            print("You have fallen to a Goblin!")


    elif raw_input == "3":
        print("You ran like a coward!")
        break

    else:
        print("Invalid input {}".format(raw_input))


