#-----------------------------------------------------------------------------
# Name:        Ultimate Frisbee Tracker (main.py)
# Purpose:     Determines your skills in Ultimate Frisbee using your average scores per game. 
#              Creates a plan for improvement
#
# Author:     Uday Saini  
# Created:    20-Feb-2024
# Updated:    23-Feb-2024 
#-----------------------------------------------------------------------------


#Asks users for the number of games they wish to calculate. Only accepts positive numbers from 1-20.
print("To determine your skill at Ultimate Frisbee we will first look at your average scores per game")
numGames = int(input("How many games do you wish to calculate? "))
while numGames <= 0 or numGames > 20:
    print("This number is invalid. Keep in mind it should be between 1 and 20 games.")
    numGames = int(input("How many games do you wish to calculate? ")) 


#Asks uses for loop to ask user for their number of scores each game. Uses division in order to find out the average
total = 0
for game in range(1, numGames+1):
    numGoals = int(input(f"How many goals did you score in game {game}? "))
    while numGoals < 0:
        print("Invalid input. Please try again. ")
        numGoals = int(input(f"How many goals did you score in game {game}? "))
    total += numGoals
averageGoals = round(total/numGames, 2)
print("On average you score " + str(float(averageGoals)) + " goals per game")
print("Now lets look at how many goals you missed\n")


#uses for loop to ask user for number of points they missed. Uses division to find the average
totalMissed = 0
for missed in range(1, numGames+1):
    numMissed = int(input(f"How many passes did you miss in the endzone in game {missed}? "))
    while numMissed < 0:
        print("Invalid input. Please try again")
        numMissed = int(input(f"How many passes did you miss in the endzone in game {missed}? "))
    totalMissed += numMissed
averageMissed = round(totalMissed/numGames, 2)
print("On average you miss " + str(float(averageMissed)) + " goals per game")
print("Your ratio of goals to misses is " + str(float(averageGoals)) + ":" + str(float(averageMissed)) + "\n")


#asks the user if they wish to continue with the following section. While loop to prevent invalid input. If no then following section is skipped.
answer = input("Do you wish to improve you average goals per game (yes or no) ")
while answer != "yes" and answer != "no":
    print("This is an invalid input. Please answer with yes or no")
    answer = input("Do you wish to improve you average goals per game (yes or no) ")

if answer == "no":
    print("Ok let's move on")

elif answer == "yes":
    #asks the user to set a goal for themselves and the amount of games they hope to achieve it.
    newGoal = int(input("What are you hoping for you new average goals per game? "))
    while newGoal <= 0:
        print("This number is invalid. Please try again.")
        newGoal = int(input("What are you hoping for you new average goals per game? "))

    newnumGames = int(input("In how many games do you hope to achieve it? "))
    while newnumGames <= 0 or newnumGames > 20:
        print("Keep between 1-20")
        newnumGames = int(input("In how many games do you hope to achieve it? "))

    newTotal = 0

    #asks the user the number of goals they scored each game and checks to see if it matched with their goal.
    for score in range(1, newnumGames+1):
        newnumGoals = int(input(f"How many goals did you score in game {score}? "))
        while newnumGoals < 0:
            print("This input is invalid. Please try again.")
            newnumGoals = int(input(f"How many goals did you score in game {score}? ")) 
        newTotal += newnumGoals

    newAverage = round(newTotal/newnumGames, 2)
    print("Your new average is " + str(newAverage) + "\n")

    #Congratulations to the user if they achieve their goal.
    if newAverage >= newGoal:
        print("Congratulations! You achieved your goal")

    #Asks the user if they wish to attempt their goal if they did not achieve it.
    while newAverage < newGoal:
        print("You did not achieve your goal. Don't give up!")
        answer = input("Do you wish to improve you average goals per game (yes or no) ")

        #Asks if the user wants to continue as well as prevents invalid inputs.
        while answer != "yes" and answer != "no":
            print("This is an invalid input. Please answer with yes or no")
            answer = input("Do you wish to improve you average goals per game (yes or no) ")

        if answer == "no":
            print("Ok let's move on")
            break

        elif answer == "yes":
            newGoal = int(input("What are you hoping for you new average goals per game? "))
            while newGoal <= 0:
                print("This input is invalid. Please try again.")
                newGoal = int(input("What are you hoping for you new average goals per game? "))

            newnumGames = int(input("In how many games do you hope to achieve it? "))
            while newnumGames <= 0:
                print("This input is invalid. Please try again.")
                newnumGames = int(input("In how many games do you hope to achieve it? "))

            newTotal = 0
            for score in range(1, newnumGames+1):
                newnumGoals = int(input(f"How many goals did you score in game? {score} "))
                while newnumGoals < 0:
                    print("This input is invalid")
                    newnumGoals = int(input(f"How many goals did you score in game? {score} "))
                newTotal += newnumGoals

            newAverage = round(newTotal/newnumGames, 2)
            print("Your new average is " + str(float(newAverage)) + " goals per game")

            if newAverage >= newGoal:
                print("Congratulations! You achieved your goal \n")
                break

newAnswer = input("Do you wish to continue? ")

#eliminates invalid inputs
while newAnswer != "yes" and newAnswer != "no":
    print("This input is invalid.")
    newAnswer = input("Do you wish to continue? ")

if newAnswer == "no":
    print("This brings us to the end of the Ultimate Frisbee Tracker. Thanks for trying this out, Goodbye!")

if newAnswer == "yes":
    print("Great, now let's look at your wins and losses")
    totalGames = int(input("How many games do you wish to calculate? "))
    while totalGames <= 0:
        print("This input is invalid. Please try again.")
        totalGames = int(input("How many games do you wish to calculate? "))

    numWins = int(input("How many of those game did you win? "))
    while numWins < 0 or numWins > totalGames:
        print("This number is invalid. Please try again.")
        numWins = int(input("How many of those game did you win? "))

    winPercent = numWins/totalGames * 100
    print("You won " + str(winPercent) + " % of your games ")

    numLosses = (totalGames - numWins) / totalGames * 100
    print("You lost " + str(float(numLosses)) + " % of your games \n")

    userAnswer = input("Do you want to improve your percentage of wins? (yes or no) ")
    while userAnswer != "yes" and userAnswer != "no":
        print("This input is invalid.")
        userAnswer = input("Do you want to improve your percentage of wins? (yes or no) ")

    if userAnswer == "no":
        print("This brings us to the end of the Ultimate Frisbee Tracker. Thanks for trying this out, Goodbye!")

    elif userAnswer == "yes":
        winGoal = int(input("What win percentage are you hoping to have? "))
        while winGoal < 0 or winGoal > 100:
            print("This input is invalid.")
            winGoal = int(input("What win percentage are you hoping to have? "))

        newtotalGames = int(input("In how many games do you hope to achieve it? "))
        while newtotalGames <= 0:
            print("This input is invalid")
            newtotalGames = int(input("In how many games do you hope to achieve it? "))

        newnumWins = int(input("How many of those games did you win? "))
        while newnumWins < 0 or newnumWins > newtotalGames:
            print("This input is invalid")
            newnumWins = int(input("How many of those games did you win? "))

        newWinpercent = (newnumWins / newtotalGames) * 100

        if newWinpercent >= winGoal:
            print("Congratulations! You achieved your goal!")
            print("This brings us to the end of the Ultimate Frisbee Tracker. Thanks for trying this out, Goodbye!")

        while newWinpercent < winGoal:
            print("You did not achieve your goal. Don't give up!")
            userAnswer = input("Do you want to improve your percentage of wins? (yes or no) ")
            while userAnswer != "yes" and userAnswer != "no":
                print("This input is invalid.")
                userAnswer = input("Do you want to improve your percentage of wins? (yes or no) ")

            if userAnswer == "no":
                print("This brings us to the end of the Ultimate Frisbee Tracker. Thanks for trying this out, Goodbye!")
                break

            elif userAnswer == "yes":
                winGoal = int(input("What win percentage are you hoping to have? "))
                while winGoal < 0 or winGoal > 100:
                    print("This input is invalid.")
                    winGoal = int(input("What win percentage are you hoping to have? "))

                newtotalGames = int(input("In how many games do you hope to achieve it? "))
                while newtotalGames <= 0:
                    print("This input is invalid")
                    newtotalGames = int(input("In how many games do you hope to achieve it? "))

                newnumWins = int(input("How many of those games did you win? "))
                while newnumWins < 0 or newnumWins > newtotalGames:
                    print("This input is invalid")
                    newnumWins = int(input("How many of those games did you win? "))

                newWinpercent = (newnumWins / newtotalGames) * 100

                if newWinpercent >= winGoal:
                    print("Congratulations! You achieved your goal!")
                    print("This brings us to the end of the Ultimate Frisbee Tracker. Thanks for trying this out, Goodbye!")
                    break
