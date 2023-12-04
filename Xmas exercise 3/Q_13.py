import utility

numbers = []
for _ in range(5) :
    numbers.append(utility.entryCheck("Enter a number: ", r"^-?[0-9]+$", "ENTER A VALID NUMBER!"))
    
print(sum(list(map(int, numbers))))