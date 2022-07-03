
#Player Character
import random as r
r.seed()
class Character():
    def __init__(self, name, max_hp, cur_hp,speed,armor,attack,accuracy,evade) -> None:
        self.name = name
        self.max_hp = max_hp
        self.cur_hp = cur_hp
        self.speed = speed
        self.armor = armor
        self.attack = attack
        self.accuracy = accuracy
        self.evade = evade
# creating a shipmate subclass from Character
class Crewmate(Character):
    def __init__(self, name, max_hp, cur_hp, speed, armor, attack,accuracy,evade) -> None:
        super().__init__(name, max_hp, cur_hp, speed, armor, attack,accuracy,evade)

class Weapons():  
    def __init__(self, name, range,damage,num_uses) -> None:
        self.name = name
        self.range = range 
        self.damage = damage
        self.num_uses = num_uses

# crew weapons
Shotgun = Weapons('Shotgun',2,50,4)
print(Shotgun.damage)  

AutoRifle = Weapons('AutoRifle',5,35,6)
print(AutoRifle.damage)   

Grenade = Weapons('Grenade',4,120,3)
print(Grenade.damage)  

Flamer = Weapons('Flamer',4,80,6)

# Xeno weapons

Slash = Weapons('Slash',1,80,10)
print(Slash.damage)  

TailSlash = Weapons('TailSlash',3,80,10)
print(TailSlash.damage)   

MouthStrike = Weapons('MouthStrike',2,80,10)
print(MouthStrike.damage)  
# acid blood costs 
AcidBlood = Weapons('Flamer',4,120,10)

# creating q Xeno sub-class from the Character 
class Enemy(Character):
    def __init__(self, name, max_hp, cur_hp, speed, armor, attack,accuracy,evade) -> None:
        super().__init__(name, max_hp, cur_hp, speed, armor, attack,accuracy,evade)



# stat scales (1-100,1-100,1-10, 1-100,0-100,1-10)   
Ripley = Crewmate('Ripley',100,100,9,0,1,10,10)

Xenomorph = Enemy('Xenomorph',100,100,9,100,30,8,7)
# def crew and xeno attack

# finish making comparisons for spped. evade, etc....


    


# def CrewMoveSecond():

def XenoMoveFirst():
    print("The Xenomorph moves!")
attack = r.randint(0,4) 
print(attack)
if attack == "1":
        Ripley.cur_hp = Ripley.cur_hp - Slash.damage
        print(Ripley.cur_hp)
elif attack == "2":
    Ripley.cur_hp = Ripley.cur_hp - TailSlash.damage
    print(Ripley.cur_hp)
elif attack == "3":
    Ripley.cur_hp = Ripley.cur_hp - MouthStrike.damage
    print(Ripley.name , "has" ,Ripley.cur_hp,  " hp left!")
elif attack == "4":
    Ripley.cur_hp = Ripley.cur_hp - AcidBlood.damage
    print(Ripley.cur_hp)
else:
    print("The xenomorph missed!")    

# def XenoMoveSecond():

def XenoMoveSecond():
    print("The Xenomorph moves!")
    attack = r.randint(0,4) 
    print(attack)
    if attack == "1":
            Ripley.cur_hp = Ripley.cur_hp - Slash.damage
            print(Ripley.cur_hp)
    elif attack == "2":
        Ripley.cur_hp = Ripley.cur_hp - TailSlash.damage
        print(Ripley.cur_hp)
    elif attack == "3":
        Ripley.cur_hp = Ripley.cur_hp - MouthStrike.damage
        print(Ripley.name , "has" ,Ripley.cur_hp,  " hp left!")
    elif attack == "4":
        Ripley.cur_hp = Ripley.cur_hp - AcidBlood.damage
        print(Ripley.cur_hp)
    else:
        print("The xenomorph missed!")   

# if crew speed > xeno speed
def RipleyMoveFirst():
    attack = input("What's your move?")
    print("1." , Shotgun.name , "2." , AutoRifle.name , "3." , Grenade.name , "4." , Flamer.name)
    if attack == "1":
        Xenomorph.cur_hp = Xenomorph.cur_hp - Shotgun.damage
        print('The', Xenomorph.name , "has" ,Xenomorph.cur_hp,  " hp left!")
    elif attack == "2":
        Xenomorph.cur_hp = Xenomorph.cur_hp - AutoRifle.damage
        print('The', Xenomorph.name , "has" ,Xenomorph.cur_hp,  " hp left!")
    elif attack == "3":
        Xenomorph.cur_hp = Xenomorph.cur_hp - Grenade.damage
        print('The', Xenomorph.name , "has" ,Xenomorph.cur_hp,  " hp left!")
    elif attack == "4":
        Xenomorph.cur_hp = Xenomorph.cur_hp - Flamer.damage
        print('The', Xenomorph.name , "has" ,Xenomorph.cur_hp,  " hp left!")


# if crew speed > xeno speed
def RipleyMoveSecond():
    attack = input("What's your move?")
    print("1." , Shotgun.name , "2." , AutoRifle.name , "3." , Grenade.name , "4." , Flamer.name)
    if attack == "1":
        Xenomorph.cur_hp = Xenomorph.cur_hp - Shotgun.damage
        print('The', Xenomorph.name , "has" ,Xenomorph.cur_hp,  " hp left!")
    elif attack == "2":
        Xenomorph.cur_hp = Xenomorph.cur_hp - AutoRifle.damage
        print('The', Xenomorph.name , "has" ,Xenomorph.cur_hp,  " hp left!")
    elif attack == "3":
        Xenomorph.cur_hp = Xenomorph.cur_hp - Grenade.damage
        print('The', Xenomorph.name , "has" ,Xenomorph.cur_hp,  " hp left!")
    elif attack == "4":
        Xenomorph.cur_hp = Xenomorph.cur_hp - Flamer.damage
        print('The', Xenomorph.name , "has" ,Xenomorph.cur_hp,  " hp left!")

# creating the move order logic  

def who_moves():
    ripley_init = (Ripley.speed + (Ripley.speed * (r.random * 5)))  
    xeno_init = (Ripley.speed + (Ripley.speed * (r.random * 5))) 
    if xeno_init > ripley_init:
        XenoMoveFirst()
    elif ripley_init > xeno_init: 
        RipleyMoveFirst()
    else:
        print('initiatives are equal!')
        break






        


    # def display_player_character():
    #     print(Character.name,Character.sex,Character,Character.max_hp,Character.cur_hp,Character.speed,Character.armor)
        

# #Enemy class
# class Enemy():
#     def __init__(self, monster, max_hp, cur_hp,speed,armor,attack) -> None:
#         self.monster = monster
#         self.max_hp = max_hp
#         self.cur_hp = cur_hp
#         self.speed = speed
#         self.armor = armor
#         self.attack = attack
        
#     def display_player_character2():
#         print(Enemy.monster,Enemy.max_hp,Enemy.cur_hp,Enemy.speed,Enemy.armor)  

# combat function

# Ripley = Character('Ripley', 50, 50, 1 , 0, 0)

# Xenormorph = Enemy('Xenomorph', 50, 50, 1, 20, 0)


#ripley attacks alien 
# Xenormorph.cur_hp = Xenormorph.cur_hp - Ripley.attack
# print(f'The xeno has' , Xenormorph.cur_hp , 'health left!')

# #alien attacks Ripley
# Ripley.cur_hp = Ripley.cur_hp - Xenormorph.attack
# print(f'Ripley has' , Ripley.cur_hp ,'health left!')

# next task:find out how to access the attack traits with EQUIPABLE weapons, and give the alien some kind of weapon classes??