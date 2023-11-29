import utility

num1 = utility.entryCheck("Enter marks in subject1: ", r"^-?\d*\.?\d{1,3}$", Type="float")
num2 = utility.entryCheck("Enter marks in subject2: ", r"^-?\d*\.?\d{1,3}$", Type="float")
num3 = utility.entryCheck("Enter marks in subject3: ", r"^-?\d*\.?\d{1,3}$", Type="float")

max = num1

if max < num2 :
    max = num2 
if max < num3 :
    max = num3

print(f"{max} is the greatest")
