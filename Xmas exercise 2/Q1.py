import utility

number = utility.entryCheck("Enter a number: ", "^-?[0-9]+$")

if number % 2 == 0 :
    print(f"{number} is even!")
else :
    print(f"{number} is odd!")