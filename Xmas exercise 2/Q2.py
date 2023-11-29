import utility

age = utility.entryCheck("Enter your age: ", "^[0-9]{2}$")

if age > 17 :
    print("You can vote!!")
else :
    print("you cannot vote! you are a BABY!")