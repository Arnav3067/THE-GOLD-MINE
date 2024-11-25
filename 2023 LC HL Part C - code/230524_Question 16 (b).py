import random

totalScore = 0

def GetScore(diff) :
    if (diff <= 30) :
        print("You have scored 30 points")
        return 30
    elif (diff > 30) :
        print("You lost 30 points")
        return -30
    elif (diff == 0) :
        print("JackPot!! You scored 100 points")
        return 100

def GuessGame() :
    global totalScore
    secretNumber =  random.randint(1, 100)
    userGuess = int(input("Enter your Guess: "))
    diff = abs(secretNumber - userGuess)
    
    print(f"The secret number was {secretNumber}. Your guess was {userGuess}. The difference was {diff}")

    totalScore += GetScore(diff)

    print(f"Your total score is {totalScore}")

    userChoice = input("Do you wish to continue [Y/N]: ")

    if (userChoice.lower() == "y") : 
        GuessGame()

GuessGame()

    

