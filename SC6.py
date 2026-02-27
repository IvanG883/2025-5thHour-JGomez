#Name: Ivan Gomez
#Class: 5th Hour
#Assignment: Scenario 6

import random

#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Semester Project 1 using classes instead of dictionaries, include and refactor
#the combat test code below as well.)

class Character:
    def __init__(self,HP,init,AC,Atk,Damage):
        self.HP = HP
        self.init = init
        self.AC = AC
        self.Atk = Atk
        self.Damage = Damage


#Hero Characters
Laezel = Character(48,1,17,6,random.randint(1,6) + random.randint(1,6 ) + 3)
Shadowheart = Character(40,1,18,4,random.randint(1,6) + 3)
Gale = Character(32,1,14,6,random.randint(1,10) + random.randint(1,10))
Astarion = Character(40,3,14,5,random.randint(1,8) + random.randint(1,6) + 4)

#Enemy Characters
Goblin = Character(7,0,12,4,random.randint(1,6) + 2)
Orc = Character(15,1,13,5,random.randint(1,12) + 3)
Troll = Character(84,1,14,5,random.randint(1,6) + random.randint(1,6) + 4)
Mindflayer = Character(71,1,15,7,random.randint(1,10) + random.randint(1,10) + 4)
Dragon = Character(127,2,18,7,random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 4)

Player1 = random.randint(1,20) + Shadowheart.init
player2 = random.randint(1,20) + Orc.init
if Player1 >=  player2:
    print("shadowheart goes first")
    Player1first = True
else :
    print("Orc goes first")
    Player1first = False


while Shadowheart.HP > 0 and Orc.HP > 0:
    if Player1first == True:
        Player1atk =random.randint(1,20)
        print(Player1atk)
        if Player1atk == 20:
            Orc.HP -= (Shadowheart.Damage*2)
            print(f"Shadowheart hits Orc for {Shadowheart.Damage*2}")
        elif Player1atk == 1:
            print("Roll natural 1, Missed attack")
        elif Player1atk + Shadowheart.Atk >= Orc.AC:
            Orc.HP -= Shadowheart.Damage
            print(f"Shadowheart hits Orc for {Shadowheart.Damage}")
        else:
           print("Shadowheart missed thir attack")

        Player2atk = random.randint(1,20)
        print(Player2atk)
        if Player2atk == 20:
            Shadowheart.HP -= (Orc.Damage*2)
            print(f"Orc hits Shadowheart for {(Orc.Damage*2)}")
        elif Player2atk == 1:
            print("Roll natural 1, Missed attack")
        elif Player2atk + Orc.Atk >= Shadowheart.AC:
            Shadowheart.HP -= (Orc.Damage*2)
            print(f"Orc hits Shadowheart for {(Orc.Damage)}")
        else:
            print("Orc missed thir attack")

    else:
        Player2atk = random.randint(1,20)
        print(Player2atk)
        if Player2atk == 20:
            Shadowheart.HP -= (Orc.Damage*2)
            print(f"Orc hits Shadowheart for {(Orc.Damage*2)}")
        elif Player2atk == 1:
            print("Roll natural 1, Missed attack")
        elif Player2atk + Orc.Atk >= Shadowheart.AC:
            Shadowheart.HP -= (Orc.Damage*2)
            print(f"Orc hits Shadowheart for {(Orc.Damage)}")
        else:
            print("Orc missed thir attack")

        Player1atk =random.randint(1,20)
        print(Player1atk)
        if Player1atk == 20:
            Orc.HP -= (Shadowheart.Damage*2)
            print(f"Shadowheart hits Orc for {(Shadowheart.Damage*2)}")
        elif Player1atk == 1:
            print("Roll natural 1, Missed attack")
        elif Player1atk + Shadowheart.Atk >= Orc.AC:
            Orc.HP -= (Shadowheart.Damage)
            print(f"Shadowheart hits Orc for {(Shadowheart.Damage)}")
        else:
           print("Shadowheart missed thir attack")
else:
    if Shadowheart.HP < 0:
        print("Shadowheart died")
    else:
        print("Orc died")

