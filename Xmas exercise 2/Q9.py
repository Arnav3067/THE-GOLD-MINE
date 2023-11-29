import utility
import math

while True :

    a = utility.entryCheck("Enter coefficient a: ", r"^-?\d*\.?\d{1,3}$", "ValueError: invalid entry for a", Type="float")
    b = utility.entryCheck("Enter coefficient b: ", r"^-?\d*\.?\d{1,3}$", "ValueError: invalid entry for b", Type="float")
    c = utility.entryCheck("Enter coefficient c: ", r"^-?\d*\.?\d{1,3}$", "ValueError: invalid entry for c", Type="float")

    delta = (b**2) - (4*a*c)

    if delta < 0 :
        print("MathError: complex roots")
    else :
        break
        
print(f"x = {(b + math.sqrt(delta))/2*a} and x = {(b - math.sqrt(delta))/2*a}")