import utility

number = utility.entryCheck("Enter a number: ", r"^-?\d*\.?\d{1,3}$", Type='float')

if number > 0 :
    print("positive")
elif number < 0 :
    print("negative")
else :
    print("its zero")