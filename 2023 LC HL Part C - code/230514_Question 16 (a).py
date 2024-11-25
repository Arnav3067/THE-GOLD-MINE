# Question 16(a)
# Examination Number: 230514 Arnav Kothari

import random

difficulty = {
    "H" : range(1, 101),
    "E" : range(1, 5)
}

def guess_game(max_guesses_allowed, userDifficulty):

    if (difficulty.__contains__(userDifficulty)) :
        secret_number = random.choice(difficulty[userDifficulty])
    else :
        secret_number = random.choice(difficulty["E"])

    guess_count = 0
    userGuesses = []
    user_guess = 0

    while (user_guess != secret_number):
        user_guess = int(input("Enter your guess: "))
        guess_count += 1 #Increase guess_count by 1
        
        if userGuesses.__contains__(user_guess) : 
            print("You already entered this")
        else :
            userGuesses.append(user_guess)

        if user_guess < secret_number :
            print("Sorry! Your guess was too low")

        elif user_guess > secret_number :
            print("Sorry! Your guess was too high")

        else :
            print("Congratulations! You win!")
            print(f"You took {guess_count} guesses!")
        
        if guess_count > max_guesses_allowed :
            print("You ran out of guesses")
            break

print("Welcome to the guessing game!")
maxNumberOfGuesses = int(input("Enter the maximum number of guesses possible: "))
userDifficulty = input("Enter difficulty E(asy) or H(ard) : ")

guess_game(maxNumberOfGuesses, userDifficulty)