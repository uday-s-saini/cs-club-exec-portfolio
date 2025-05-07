import random

# function for stealing the ball which is randomized
def steal(possessing_team):
    # code if the enemy is trying to steal from the player
    if possessing_team == "Player":
        stealing_team = "Enemy"
        steal_result = random.choice([possessing_team, stealing_team])
        if steal_result == possessing_team:
            print("They failed, You keep the ball.")
            possessing_team = "Player"
            return possessing_team
        # changes the possession of the ball
        else:
            print("The enemy stole the ball")
            possessing_team = "Enemy"
            return possessing_team

    # code if the player is trying to steal from the enemy
    if possessing_team == "Enemy":
        stealing_team = "Player"
        steal_result = random.choice([possessing_team, stealing_team])
        if steal_result == possessing_team:
            print("You failed. The enemy keeps the ball.")
            possessing_team = "Enemy"
            return possessing_team
        # changes the possession of the ball
        else:
            print("You stole the ball")
            possessing_team = "Player"
            return possessing_team

# function for shooting the ball
def shoot(possessing_team, shot_type, player_score, enemy_score):
    # variables to determine if the shot scored or missed, will be randomized in a list
    score = "Scored"
    miss = "Miss"
    miss_two = "miss"
    # if the player is trying to shoot
    if possessing_team == "Player":
        print("You attempt the shot!")
        # code for a 2 pointer
        if shot_type == "2":
            shot_result = random.choice([score, miss])
            if shot_result == score:
                player_score += 2
                possessing_team = "Enemy"
                print(f"You Scored! The Score is: {player_score} - {enemy_score}")
                return [possessing_team, player_score, enemy_score]
            else:
                print("You missed the shot")
                possessing_team = "Enemy"
                return [possessing_team, player_score, enemy_score]
        # code for a 3 pointer
        if shot_type == "3":
            shot_result = random.choice([score, miss, miss_two])
            if shot_result == score:
                player_score += 3
                possessing_team = "Enemy"
                print(f"You scored. The score is {player_score} - {enemy_score}")
                return [possessing_team, player_score, enemy_score]
            else:
                print("You missed the shot")
                possessing_team = "Enemy"
                return [possessing_team, player_score, enemy_score]
    # if the enemy is trying to shoot the ball
    if possessing_team == "Enemy":
        print("The enemy takes the shot")
        # code for a 2 pointer
        if shot_type == "2":
            shot_result = random.choice([score, miss])
            if shot_result == score:
                enemy_score += 2
                possessing_team = "Player"
                print(f"The enemy scored! The Score is: {player_score} - {enemy_score}")
                return [possessing_team, player_score, enemy_score]
            else:
                print("They missed the shot")
                possessing_team = "Player"
                return [possessing_team, player_score, enemy_score]
        # code for a 3 pointer
        if shot_type == "3":
            shot_result = random.choice([score, miss, miss_two])
            if shot_result == score:
                enemy_score += 3
                possessing_team = "Player"
                print(f"The enemy scored! The score is {player_score} - {enemy_score}")
                return [possessing_team, player_score, enemy_score]
            else:
                print("You missed the shot")
                possessing_team = "Player"
                return [possessing_team, player_score, enemy_score]

# code for a foul, loops twice for 2 shots
def foul(foul_victim, player_score, enemy_score):
    # variables to determine if the shot goes in
    hit = "hit"
    brick = "brick"
    # if the player is shooting
    if foul_victim == "Player":
        print("You take 2 shots")
        for shot in range(2):
            print("You take the shot")
            foul_result = random.choice([hit, brick])
            if foul_result == hit:
                player_score += 1
                print(f"You scored. The score is {player_score} - {enemy_score}")
            else:
                print("You missed")
        possessing_team = "Enemy"
        return ([possessing_team, player_score, enemy_score])
    # if the enemy is shooting
    if foul_victim == "Enemy":
        print("The enemy takes 2 shots")
        for shot in range(2):
            print("The enemy takes the shot")
            foul_result = random.choice([hit, brick])
            if foul_result == hit:
                enemy_score += 1
                print(f"The enemy scored! The score is {player_score} - {enemy_score}")
            else:
                print("The enemy missed missed")
        possessing_team = "Player"
        return ([possessing_team, player_score, enemy_score])

print("You will be playing basketball against the computer. The first to 5 points win. ")
user_input = input("Enter anything to continue: ")
print("Time for the Tip Off! ")

# key variables
player_team = "Player"
enemy_team = "Enemy"
starting_team = random.choice([player_team, enemy_team])
player_score = 0
enemy_score = 0
steal_move = "steal"

# determines who starts with the ball
if starting_team == "Player":
    print("You won the tip off. You have the ball.")
    possessing_team = "Player"
if starting_team == "Enemy":
    print("You lost the tip off. The enemy has the ball.")
    possessing_team = "Enemy"

# loops the game until someone reaches the points required
while player_score < 5 and enemy_score < 5:
    # scenario if player has the ball
    if possessing_team == "Player":
        print("You move up the court")
        enemy_move = random.choice([steal_move, foul])
        # if the player is fouled
        if enemy_move == foul:
            print("The enemy fouled you!")
            possessing_team, player_score, enemy_score = foul(foul_victim="Player", player_score=player_score, enemy_score=enemy_score)
            if player_score >= 5:
                print("You won the game! ")
                break
            if enemy_score >= 5:
                print("You lost the game")
                break
        # if the ball is stolen
        if enemy_move == steal_move:
            print("The enemy attempts a steal")
            possessing_team = steal(possessing_team="Player")
        # the player shoots
        if possessing_team == "Player":
            shot_type = input("Would you like to attempt a 2 pointer or a 3 pointer? (Enter 2 or 3): ")
            while shot_type != "2" and shot_type != "3":
                print("Invalid Input. Please try again")
                shot_type = input("Would you like to attempt a 2 pointer or a 3 pointer? (Enter 2 or 3): ")
            possessing_team, player_score, enemy_score = shoot(possessing_team="Player", player_score=player_score, enemy_score=enemy_score, shot_type=shot_type)
            if player_score >= 5:
                print("You won the game! ")
                break
            if enemy_score >= 5:
                print("You lost the game")
                break

    # scenario if the enemy has the ball
    if possessing_team == "Enemy":
        print("The enemy moves up the court")
        # players choice on what to do
        play_choice = input("Would you like to Steal or Defend? ")
        while play_choice != "steal" and play_choice != "defend":
            print("Invalid Input. Please try again")
            play_choice = input("Would you like to Steal or Defend? ")
        # player tries to steal
        if play_choice == "steal":
            print("You attempt a steal")
            possessing_team = steal(possessing_team="Enemy")
        # the enemy shoots
        if possessing_team == "Enemy":
            shot_type = random.choice(["2", "3"])
            possessing_team, player_score, enemy_score = shoot(possessing_team="Enemy", player_score=player_score, enemy_score=enemy_score, shot_type=shot_type)
            if player_score >= 5:
                print("You won the game! ")
                break
            if enemy_score >= 5:
                print("You lost the game")
                break
        # if the player plays defense, results in a steal or foul
        if play_choice == "defend":
            defend_move = random.choice([steal_move, foul])
            if defend_move == steal_move:
                print("You stole the ball")
                possessing_team = "Player"
            if defend_move == foul:
                print("You fouled the enemy")
                possessing_team, player_score, enemy_score = foul(foul_victim="Enemy", player_score=player_score, enemy_score=enemy_score)
                if player_score >= 5:
                    print("You won the game! ")
                    break
                if enemy_score >= 5:
                    print("You lost the game")
                    break