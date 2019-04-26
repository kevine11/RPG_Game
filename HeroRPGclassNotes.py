#####
#!/usr/bin/env python
# In this simple RPG game, the hero fights the goblin. He has the options to:
# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

###### SELF NOTES: add crit chance, add defense power, add block

# class Hero(object):
#     def __init__ (self, heroHealth, heroPower):
#     self.heroHealth = heroHealth
#     self.heroPower = heroPower
    
# class Goblin(object):
#     def __int__(self, goblinHealth, goblinPower):
#     self.goblinHealth = goblinHealth
#     self.goblinPower = goblinPower
    
# goblin_health -= hero_power
# print("You do {} damage to the goblin.".format(hero_power))
# if goblin_health <= 0:
# print("The goblin is dead.")
# elif raw_input == "2":
# pass
# elif raw_input == "3":
# print("Goodbye.")
# break
# else:
# print("Invalid input {}".format(raw_input))
# if goblin_health > 0:
    




# ######## RPG TEMPLATE

# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

# while goblin_health > 0 and hero_health > 0:
# print("You have {} health and {} power.".format(hero_health, hero_power))
# print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
# print()
# print("What do you want to do?")
# print("1. fight goblin")
# print("2. do nothing")
# print("3. flee")
# print("> ", end=' ')
# raw_input = input()
# if raw_input == "1":
# # Hero attacks goblin
#             goblin_health -= hero_power
# print("You do {} damage to the goblin.".format(hero_power))
# if goblin_health <= 0:
# print("The goblin is dead.")
# elif raw_input == "2":
# pass
# elif raw_input == "3":
# print("Goodbye.")
# break
# else:
# print("Invalid input {}".format(raw_input))
# if goblin_health > 0:
# # Goblin attacks hero
#             hero_health -= goblin_power
# print("The goblin does {} damage to you.".format(goblin_power))
# if hero_health <= 0:
# print("You are dead.")
# main()

######### FRIDAY RPG CLASS NOTES

class Character(object):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def printMyself(self):
        print("I am a class!")


class Hero(Character):
    def __init__(self, health, power):
        super(Hero, self).__init__(health, power)

    def printMyself(self):
        print("I am the Hero")

class Goblin(Character):
    pass

    

hero = Hero(10,5)
goblin = Goblin(8,2)

print(hero.health)
print(Character.printMyself)