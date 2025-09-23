#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.
Creature = {
    "creature_1" : {
        "Name" : "Zombie",
        "damage" : 7,
        "poison" : True
    },
    "creature_2" : {
        "Name" : "Spider",
        "damage" : 3,
        "poison" : True

    },
    "creature_3" : {
        "Name" : "Goblin",
        "damage" : 5,
        "poison" : False
    },
    "creature_4" : {
        "Name" : "stone_golem",
        "damage" : 15,
        "poison" : False
    },
    "creature_5" : {
        "Name" : "Wolf",
        "damage" : 5,
        "poison" : False
    },
}

Enemy_damage = 0
print(f"enemy's current damage {Enemy_damage}")
Enemy_damage += Creature["creature_1"]["damage"]
print(f"enemy's current damage {Enemy_damage}")
Enemy_damage += Creature["creature_2"]["damage"]
print(f"enemy's current damage {Enemy_damage}")
Enemy_damage += Creature["creature_3"]["damage"]
print(f"enemy's current damage {Enemy_damage}")
Enemy_damage += Creature["creature_4"]["damage"]
print(f"enemy's current damage {Enemy_damage}")
Enemy_damage += Creature["creature_5"]["damage"]
print(f"enemys current damage {Enemy_damage}")