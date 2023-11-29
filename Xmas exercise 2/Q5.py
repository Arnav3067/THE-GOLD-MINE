import utility

age = utility.entryCheck("Enter a number: ", "^-?[0-9][0-9]?$")

if age <= 0 :
    print("you are not even born yet!")
elif 0 < age <= 12 :
    print("you are a child of god")
elif 13 <= age < 20 :
    print("You are Gen-z")
elif 20 <= age < 60 :
    print("You are an adult seeking the truths of this world\neither that or you are still living with your parents")
else :
    print("You are a senior citizen who is angry at the clouds")
