class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def Attack(self,enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if enemy.health <= 0:
            print("The goblin is dead.")

    def Alive(self):
        return self.health > 0

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def Attack(self,enemy):
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if enemy.health <= 0:
            print("You are dead.")

    def Alive(self):
        return self.health > 0

hero = Hero(10, 5)
goblin = Goblin(6,2)

while goblin.health and hero.health > 0:
    print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')

    raw_input = input()

    if raw_input == "1":
        hero.Attack(goblin)

    elif raw_input == "2":
        goblin.Attack(hero)

    elif raw_input == "3":
        print("You ran like a coward!")
        break

    else:
        print("Invalid input {}".format(raw_input))


