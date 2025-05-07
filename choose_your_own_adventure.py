# IMPORT SECTION
import random
import textwrap

# GLOBAL VARIABLES
ammo = 0
has_key = False
has_gun = False
tamed_dog = False
master_key = False
minigun = False
red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"
location = "START"
begin = "BEGIN"
game_over = "GAME OVER"
finish = "FINISH"

# FUNCTION DEFINITIONS
def start_1():

    
    print(green + "#" * 15 + reset)
    print(green + f"#{begin:^13}#" + reset)
    print(green + "#" * 15 + reset)
    
    print()
    
    print(textwrap.fill( # THIS ON ITS OWN LINE.
        f"You were framed for committing a bank robbery and as a result you " + 
        f"were sentenced to life in a maximum security prison. The " +
        f"conditions are horrible and the guards are evil so you must find a "
        f"way to escape the prison alive.",
        width = 80))

    print("")
    
    print(textwrap.fill(
        f"First you must escape your cell. The guard comes to deliver food, "
        f"you can take a risk and attack the guard with the fork or wait " +
        f"until night to pick the lock.",
        width = 80))
    
    print("")
     
    print("What will you do?")
    user_choice = (input(f"\n" +
    f"1) Attack the Guard\n" +
    f"2) Pick the Lock\n" 
    f"I) Open Inventory\n" +
    f"M) Open Map\n"))
    
    if user_choice == "1":
        attack_guard_2()
        
    elif user_choice == "2":
        pick_lock_10()
        
    elif user_choice == "I":
        inventory()
        start_1()
    
    elif user_choice == "M":
        game_map()
        start_1()
        
    else:
        start_1()
        
def attack_guard_2():
    global ammo, has_key, has_gun
    print("You chose to attack the guard. Bold move.\n")
    success = random.choice([True, True, False])
    if success == True:
        print(textwrap.fill(
            f"You killed the guard and stole his keys and gun with 4 bullets. "+
            f"However you made a lot of noise and the other guards were on " +
            f"their way so you have to run. \n",
            width = 80))
        has_key = True
        has_gun = True
        ammo = 4
        guarded_hallway_4()
        
    else:
        game_over_one_3()

def game_over_one_3():
    
    print(textwrap.fill(
        f"You tried to attack the guard with your fork but the guard got the " +
        f"upper hand and shot you. You died.",
        width = 80))

    
    print(red + "#" * 15 + reset)
    print(red + f"#{game_over:^13}#" + reset)
    print(red + "#" * 15 + reset)
    
    
def guarded_hallway_4():
    global location
    location = "HALLWAY"
    print(textwrap.fill(
        f"You reach a hallway with 2 doors but there are 2 guards protecting " +
        f"each.\n ",
        width = 80))
    
    print("Which door do you want to go through?\n")
    
    user_choice = (input(f"\n" +
    f"1) Door 1\n" +
    f"2) Door 2\n" +
    f"I) Open Inventory\n" +
    f"M) Open Map\n"))
    
    if user_choice == "1":
        print("You have chosen Door 1\n")
        door_one_choice_37()
        
    
    elif user_choice == "2":
        print("You have chosen Door 2\n")
        door_two_choice_38()
        
    elif user_choice == "I":
        inventory()
        guarded_hallway_4()
        
    elif user_choice == "M":
        game_map()
        guarded_hallway_4()
        
    else:
        guarded_hallway_4()

def door_one_choice_37():
    global location
    location = "DOOR ONE"
    
    print(textwrap.fill(
            f"Will you attack the guards now or save your ammo and wait until "+
            f"night with a chance of being caught.\n",
            width = 80))
        
    user_choice = (input(f"\n" +
    f"1) Attack Now\n" +
    f"2) Wait Until Night\n"
    f"I) Open Inventory\n" +
    f"M) Open Map\n"))
        
    if user_choice == "1":
        door_one_attack_5()
            
    elif user_choice == "2":
        door_one_wait_6()
    
    elif user_choice == "I":
        inventory()
        door_one_choice_37()
        
    elif user_choice == "M":
        game_map()
        door_one_choice_37()
        
    else:
        door_one_choice_37()
            
def door_two_choice_38():
    global location
    location = "DOOR TWO"
    print(textwrap.fill(
            f"Will you attack the guards now or save your ammo and wait until "+
            f"night with a chance of being caught.\n",
            width = 80))
    user_choice = (input(f"\n" +
    f"1) Attack Now\n" +
    f"2) Wait Until Night\n"
    f"I) Open Inventory\n" +
    f"M) Open Map\n"))
        
    if user_choice == "1":
        door_two_attack_7()
            
    elif user_choice == "2":
        door_two_wait_8()
            
    elif user_choice == "3":
        door_two_wait_8()
        door_two_choice_38()
        
    elif user_choice == "M":
        game_map()
        door_two_choice_38()
    
    else:
        door_two_choice_38()
        
def door_one_attack_5():
    global ammo
    print(textwrap.fill(
        f"You chose to attack the guards at door 1. You use one bullet on "+
        f"each guard which kills them. Your ammo reduces by 2. The door is "+
        f"unlocked so you enter it and barricade it so the guards can’t "+
        f"follow you.",
        width = 80))
    
    ammo = ammo - 2
    door_one_11()
    
def door_one_wait_6():
    print("You hide in a corner and wait for the guards to leave. ")
    
    caught = random.choice([True, False, False])
    
    if caught == True:
        game_over_two_9()
        
    else:
        print("The guards have left so you enter Door 1\n")
        door_one_11()

def door_two_attack_7():
    global ammo
    print(textwrap.fill(
        f"You chose to attack the guards at door 2. You use one bullet on "+
        f"each guard which kills them. Your ammo reduces by 2. The door is "+
        f"locked and requires a guard key. ",
        width = 80))
    ammo = ammo - 2
     
    print (" ")
    
    if has_key == True:
        print(textwrap.fill(
            f"You unlock the door and go through, you make sure to barricade "+
            f"the doors so the guards can’t follow.",
            width = 80))
        door_two_20()
    
    else:
        door_one_attack_5()

def door_two_wait_8():
    
    print("You hide in a corner and wait for the guards to leave. \n")
    
    caught = random.choice([True, False, False])
    
    if caught == True:
        game_over_two_9()
    
    elif caught == False and has_key == True:
        print(textwrap.fill(
            f"The guards have left so you go to Door 2 which requires a key. " +
            f"You have the key so you enter Door 2",
            width = 80))
        door_two_20()
    
    elif caught == False and has_key == False:
        print(textwrap.fill(
            f"The guards have left so you go to Door 2 which requires a key. " +
            f"Unforntunately you do not have they key so you go through Door " +
            f"1 instead.",
            width = 80))
        door_two_20()
    
def game_over_two_9():

    print(" ")
    print(textwrap.fill(
        f"You were hiding in a corner until night however the guards passing "+
        f"by noticed you and all fired their guns at you. You die on the spot "+
        f"without a moment to react",
        width = 80))
    
    print(red + "#" * 15 + reset)
    print(red + f"#{game_over:^13}#" + reset)
    print(red + "#" * 15 + reset)
    
    
def pick_lock_10():
    global location
    location = "HALLWAY"
    
    print(textwrap.fill(
        f"You pick the lock and escape the cell. You sneak past the guards "+
        f"and reach a hallway with 2 doors. Which door do you choose?",
        width = 80))
    
    user_choice = (input(f"\n" +
    f"1) Door 1\n" +
    f"2) Door 2\n" +
    f"I) Open Inventory\n" +
    f"M) Open Map\n"))
    
    if user_choice == "1":
        print("You have chosen to go through Door 1.")
        print(" ")
        door_one_11()
    
    elif user_choice == "2":
        print(textwrap.fill(
            f"You have chosen to go through Door 2 which requires a key you "+
            f"do not have so you go through Door 1",
              width = 80))
        print(" ")
        door_one_11()
    
    elif user_choice == "I":
        inventory()
        pick_lock_10()
    
    elif user_choice == "M":
        game_map()
        pick_lock_10()
    
    else:
        pick_lock_10()
    
    

def door_one_11():
    global location
    location = "ROOM ONE"
    
    print(textwrap.fill(
        f"In the room there's a giant dog, 10 times your size. Make a sound " +
        f"and he will eat you alive. Behind the giant dog there is a door to "+
        f"the next room.",
        width = 80))
    
    print()
    
    print(textwrap.fill(
        f"You can try to sneak past the dog but the floor is very creaky. " +
        f"There is also some dog food in the corner which you can use to bait "+
        f"the dog away. Both are very risky, which do you choose?",
        width = 80))
        
    user_choice = (input(f"\n" +
    f"1) Sneak past the dog\n" +
    f"2) Leave some bait\n" +
    f"I) Open Inventory\n" +
    f"M) Open Map\n"))
    
    
    if user_choice == "1":
        print(" ")
        creaky_floor_12()
    
    elif user_choice == "2":
        print(" ")
        dog_bait_14()
    
    elif user_choice == "I":
        inventory()
        door_one_11()
    
    elif user_choice == "M":
        game_map()
        door_one_11()
    
    else:
        door_one_11()


def creaky_floor_12():
    global ammo
    
    print("You begin to sneak past the dog making sure to tread lightly \n")
    
    creak = random.randint(1,4)
    
    if creak == 4:
        print(textwrap.fill(
            f"The floor creaks and wakes up the dog and he charges straight "+
            f"at you.",
            width = 80))
        
        if ammo >= 2:
            print(textwrap.fill(
                f"You load two shots into the dog which kills him. You make "+
                f"it to the door and into the next room.",
                width = 80))
            ammo = ammo - 2
            final_room_27()
            
        elif ammo == 1:
            print("You load a shot into the dog but it doesn't die.")
            game_over_three_13()
        
        else:
            print("You have nothing to defend yourself with")
            game_over_three_13()
            
    else:
        print(textwrap.fill(
            f"You make it past the room without waking up the dog. You move "+
            f"on to the next room.",
            width = 80))
        final_room_27()

        

def game_over_three_13():
    
    print()
    print(textwrap.fill(
        f"The dog is enraged and grabs you and devours you alive until there "+
        f"is nothing left of you",
        width = 80))
    
    print()
    print(red + "#" * 15 + reset)
    print(red + f"#{game_over:^13}#" + reset)
    print(red + "#" * 15 + reset)
    
    
def dog_bait_14():
    global location
    location = "ROOM ONE"
    
    print(textwrap.fill(
        f"You use the dog food and set up a trail away from the door. The dog "+
        f"smells the food and wakes up. The dog is agitated but a bit calm " +
        f"due to the food. You can try to calm the dog or make a run for it.",
        width = 80))
    
    user_choice = (input(f"\n" +
    f"1) Calm down the dog\n" +
    f"2) Run for it\n" +
    f"I) Open Inventory\n" +
    f"M) Open Map\n"))
    
    if user_choice == "1":
        calm_dog_15()
    
    elif user_choice == "2":
        run_from_dog_17()
    
    elif user_choice == "I":
        inventory()
        dog_bait_14()
    
    elif user_choice == "M":
        game_map()
        dog_bait_14()
    
    else:
        dog_bait_14()


    

def calm_dog_15():
    global tamed_dog, ammo
    print("You attempt to calm the dog by petting it")
    
    success = random.uniform(0,4)
    
    if success >= 2.0:
        print(textwrap.fill(
            f"You successfully tamed the giant dog. He is now "+
            f"your loyal pet",
            width = 80))
        tamed_dog = True
        final_room_27()
    
    
    
   
    elif success < 2.0:
        if ammo >= 2:
            print(textwrap.fill(
                f"You failed to calm down the dog and he attacked you. You " +
                f"have your gun on you with which you load two shots into " +
                f"the dog which killed him. You then proceed into the next " +
                f"room.",
                width = 80))
            ammo = ammo - 2
            final_room_27()
        
        elif ammo == 1:
            print(textwrap.fill(
                  f"You failed to calm down the dog and he attacked you. You "+
                  f"shot at the dog but it doesn't die",
                  width = 80))
            game_over_four_16()
    
        elif ammo == 0 or has_gun == False:
            print(textwrap.fill(
              f"You failed to calm down the dog and he attacked you. You have "+
              f"nothing to defend yourself with.",
              width = 80))
            game_over_four_16()


def game_over_four_16():
   
    print(textwrap.fill(
        f"The dog pierces you with his claws and rips you apart and then" +
        f"devours what's left of you",
        width = 80))
    
    print()
    print(red + "#" * 15 + reset)
    print(red + f"#{game_over:^13}#" + reset)
    print(red + "#" * 15 + reset)
    
def run_from_dog_17():
    print("You run from the dog towards the next room \n")
    chase = random.random()
    
    if chase >= 0.5:
        print(textwrap.fill(
            f"Luckily the dog went for the bait and left you alone. You make "+
            f"it into the next room",
            width = 80))
        final_room_27()
    
    else:
        dog_chase_18()

def dog_chase_18():
    global ammo
    
    print("The dog did not go for the bait and has begun to chase you")
    
    caught = random.randrange(1,11)
    
    if caught >= 6:
        if has_gun == True and ammo >= 2:
            print(textwrap.fill(
                f"The dog has caught up to you so you pull out your gun and "+
                f"load two shots into the dog which kills it. You then "+
                f"proceed into the next room.",
                width = 80))
            ammo = ammo - 2
            final_room_27()
            
        elif has_gun == True and ammo == 1:
            print("You fire a shot at the dog but it doesn't die")
            game_over_five_19()
        
        elif has_gun == False or ammo == 0:
            print(textwrap.fill(
                f"The dog has caught up to you and you have nothing to defend "+
                f"yourself.",
                width = 80))
            game_over_five_19()
    
    else:
        print("You managed to outrun the dog and make it into the next room")
        final_room_27()


def game_over_five_19():
    
    print(textwrap.fill(
        f"The dog is mad you for waking him up so he grabs you with his paws "+
        f"and squeezes the life out of you",
        width = 80))
    
    print()
    print(red + "#" * 15 + reset)
    print(red + f"#{game_over:^13}#" + reset)
    print(red + "#" * 15 + reset)

def door_two_20():
    global location
    location = "ROOM TWO"
    
    print(textwrap.fill(
        f"You enter the room and notice its a guard room, would you like to "+
        f"go to the armory or the lounge",
        width = 80))
    
    user_choice = (input(f"\n" +
    f"1) Go to armory\n" +
    f"2) Go to lounge\n" +
    f"I) Open Inventory\n" +
    f"M) Open Map\n"))

    if user_choice == "1":
        armory_24()
    
    elif user_choice == "2":
        lounge_21()
    
    elif user_choice == "I":
        inventory()
        door_two_20()
    
    elif user_choice == "M":
        game_map()
        door_two_20()
    
    else:
        door_two_20()



   

def lounge_21():
    global location
    location = "LOUNGE"
    
    print(textwrap.fill(
        f"You enter the lounge and there are two rooms with different " +
        f"activities"))
    
    print("Would you like to?\n")
    
    user_choice = (input(f"\n" +
    f"1) Sleep\n" +
    f"2) Watch TV\n" +
    f"3) Return to guard room\n" +
    f"I) Open Inventory\n" +
    f"M) Open Map\n"))
    
    if user_choice == "1":
        sleep_22()
    
    elif user_choice == "2":
        tv_room_23()
    
    elif user_choice == "3":
        door_two_20()
        
    elif user_choice == "I":
        inventory()
        lounge_21()
    
    elif user_choice == "M":
        game_map()
        lounge_21()
    
    else:
        lounge_21()



def sleep_22():
    global location
    location = "BEDROOM"
    
    print("You go to sleep \n")
    print("Would you like to sleep more to return to main lounge")
    
    user_choice = (input(f"\n" +
    f"1) Sleep more\n" +
    f"2) Return to main lounge\n" +
    f"I) Open Inventory\n" +
    f"M) Open Map\n"))
    
    if user_choice == "1":
        sleep_22()
    
    elif user_choice == "2":
        lounge_21()
        
    elif user_choice == "I":
        inventory()
        sleep_22()
    
    elif user_choice == "M":
        game_map()
        sleep_22()
    
    else:
        sleep_22()
        
            
def tv_room_23():
    global location
    location = "TV ROOM"
    
    print("You go to the tv room and binge Netflix\n")
    print("Would you like to watch more to return to main lounge")
    
    user_choice = (input(f"\n" +
    f"1) Watch more\n" +
    f"2) Return to main lounge\n" +
    f"I) Open Inventory\n" +
    f"M) Open Map\n"))
    
    if user_choice == "1":
        tv_room_23()
    
    elif user_choice == "2":
        lounge_21()
        
    elif user_choice == "I":
        inventory()
        tv_room_23()
    
    elif user_choice == "M":
        game_map()
        tv_room_23()
    
    else:
        tv_room_23()



           
    
def armory_24():
    global location
    location = "ARMORY"
    
    print(textwrap.fill(
         f"You enter the armory and notice two locked boxes. Your guard key " +
         f"is getting weak and will break after one use. Which box will you "+
         f"choose?",
         width = 80))
     
    user_choice = (input(f"\n" +
        f"1) Box 1\n" +
        f"2) Box 2\n" +
        f"I) Open Inventory\n" +
        f"M) Open Map\n"))
    
    if user_choice == "1":
        box_one_25()
    
    elif user_choice == "2":
        box_two_26()
        
    elif user_choice == "I":
        inventory()
        armory_24()
    
    elif user_choice == "M":
        game_map()
        armory_24()
    
    else:
        armory_24()

def box_one_25():
    global master_key, has_key
    print(textwrap.fill(
        f"You open the box which breaks your key. Inside it is a master key "+
        f"which can unlock anything inside the prison. You take it and "+
        f"proceed to the next room",
        width = 80))
    print()
    
    master_key = True
    has_key = False
    final_room_27()


def box_two_26():
    global minigun, has_key
    print(textwrap.fill(
        f"You open the box which breaks your key. Inside it is a minigun " +
        f"fully loaded. You take it and proceed into the next room",
        width = 80))
    print()
    
    minigun = True
    has_key = False
    final_room_27()


def final_room_27():
    global location
    location = "FINAL ROOM"
    
    print(textwrap.fill(
        f"You enter a large room. At the end you can see the exit of the " +
        f"prison. However in between you and the exit is an army of guards " +
        f"who are on patrol. A regular gun is useless against these guards " +
        f"as they are too many. Do you want to confront them or hide until " +
        f"they leave?",
        width = 80))
    print()
    
    user_choice = (input(f"\n" +
    f"1) Confront the Guards\n" +
    f"2) Hide\n" +
    f"I) Open Inventory\n" +
    f"M) Open Map\n"))
    
    if user_choice == "1":
        if minigun == False and tamed_dog == False:
            game_over_six_28()
        
        if tamed_dog == True:
            dog_fight_29()
        
        if minigun == True:
            minigun_30()
    
    elif user_choice == "2":
        hide_33()
        
    elif user_choice == "I":
        inventory()
        final_room_27()
    
    elif user_choice == "M":
        game_map()
        final_room_27()
    
    else:
        final_room_27()



def game_over_six_28():
    
    print(textwrap.fill(
        f"You make a brave stand against the guards. However you are no " +
        f"match for them and they all fire upon you dropping you dead " +
        f"instantly.",
        width = 80))
    
    print()
    print(red + "#" * 15 + reset)
    print(red + f"#{game_over:^13}#" + reset)
    print(red + "#" * 15 + reset)
    
def dog_fight_29():
    print(textwrap.fill(
        f"You unleash the giant dog apon the guards. They are taken by " +
        f"surprise and the dog slaughters all the guards, clearing a path to " +
        f"you for freedom. You go through the gate and out of the prison.",
        width = 80))
    print()
    freedom_36()




def minigun_30():
    print(textwrap.fill(
        f"You load up your minigun and make a brave stand against the guards. "+
        f"You open fire and rain hell upon them.",
        width = 80))
    print()
    success = random.choice([True, True, True, False])
    
    if success == True:
        minigun_success_31()
    
    else:
        game_over_seven_32()




def minigun_success_31():
    print(textwrap.fill(
        f"The guards are not able to get a chance to fire back. You end up " +
        f"killing all the guards before your minigun runs out of ammo. You " +
        f"then proceed through the gate and out of the prison.",
        width = 80))
    print()
    
    freedom_36()
    
    
    
    
def game_over_seven_32():
    
    print(textwrap.fill(
        f"You keep firing on the guards, however, one of the guards is able " +
        f"to get a shot in and drop you to the ground. The surviving guards " +
        f"are enraged and mercilessly kill you.",
        width = 80))
    
    print()
    print(red + "#" * 15 + reset)
    print(red + f"#{game_over:^13}#" + reset)
    print(red + "#" * 15 + reset)
    
    
    
def hide_33():
    
    print("You hide behind a pillar and wait for the guards to leave")
    
    if master_key == True:
        master_key_35()
    
    else:
        caught = random.choice([True, False, False, False])
        
        if caught == True:
            game_over_eight_34()
        
        if caught == False:
            print(textwrap.fill(
                f"You managed to stay hidden until the guards left. You then "+
                f"proceed through the gate and out of the prison.",
                width = 80))
            print()
            freedom_36()

    


def game_over_eight_34():
    
    print(textwrap.fill(
        f"You tried to stay hidden but a guard spotted you. Suddenly the " +
        f"whole army of guards opened fire on you, killing you instantly.",
        width = 80))

    print()
    print(red + "#" * 15 + reset)
    print(red + f"#{game_over:^13}#" + reset)
    print(red + "#" * 15 + reset)

def master_key_35():
    print(textwrap.fill(
        f"You notice in the corner of the room a door requiring a key. You " +
        f"sneak to the door and use the key to open it. It reveals a hidden "+
        f"passageway you follow. You follow the passageway which leads you to "+
        f"a hidden submarine. You take the submarine to escape the prison " +
        f"and enjoy freedom.",
        width = 80))
   
    print(green + "#" * 15 + reset)
    print(green + f"#{finish:^13}#" + reset)
    print(green + "#" * 15 + reset)
    
    
def freedom_36():
    print(textwrap.fill(
        f"You make it out of the prison and find a boat that is unguarded. " +
        f"You take the boat and sail off to freedom.",
        width = 80))
    
    print(green + "#" * 15 + reset)
    print(green + f"#{finish:^13}#" + reset)
    print(green + "#" * 15 + reset)
    
def inventory():
    
    print(f"Your inventory: \n")
    
    if has_gun == True:
        print(f"Gun")
        print(f"Ammo: {ammo}")
    
    if has_key == True:
        print(f"Guard Key")
    
    if master_key == True:
        print(f"Master Key")
    
    if minigun == True:
        print(f"Minigun")
    
    print()


def game_map():
    
    
    print(f"                      [START]                                    ")
    print(f"                         |                                       ")
    print(f"                         |                                       ")
    print(f"        -------------[HALLWAY]-------------                      ")
    print(f"        |                                 |                      ")
    print(f"        |                                 |                      ")
    print(f"     [Door 1]                          [Door 2]       [TV ROOM]  ")
    print(f"        |                                 |               |      ")
    print(f"        |                                 |               |      ")    
    print(f"     [Room 1]                          [Room 2] -------[LOUNGE   ")
    print(f"        |                                 |               |      ")
    print(f"        |                                 |               |      ")    
    print(f"        |                              [Armory]       [BEDROOM]  ")
    print(f"        |                                 |                      ")
    print(f"        |---------------------------------|                      ")
    print(f"                         |                                       ")
    print(f"                    [FINAL ROOM]                                 ")
    
    print()
    print(f"Your Location: {location}")
    print()
    
# MAIN FUNCTION
start_1()
