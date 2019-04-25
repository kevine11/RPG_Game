class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self,enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if enemy.health <= 0:
            print("The goblin is dead.")

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

while goblin_health > 0 

while hero_health > 0:
pass

def attack(self,enemy):
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if enemy.health <= 0:
            print("You are dead.")

hero = Hero(10, 5)
goblin = Goblin(6,2)

hero.attack(goblin)