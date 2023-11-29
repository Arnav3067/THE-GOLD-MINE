
import utility

num1 = utility.entryCheck("Enter a number: ",  r"^-?\d*\.?\d{1,3}$", Type='float')
num2 = utility.entryCheck("Enter another number: ",  r"^-?\d*\.?\d{1,3}$", Type='float')

if num1 > num2 :
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")


