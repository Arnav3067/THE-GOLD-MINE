import utility

num1 = utility.entryCheck("Enter a number: ", r"^-?\d*\.?\d{1,3}$", Type="float")
num2 = utility.entryCheck("Enter another number: ", r"^-?\d*\.?\d{1,3}$", Type="float")
num3 = utility.entryCheck("Enter another number again: ", r"^-?\d*\.?\d{1,3}$", Type="float")

List = [num1, num2, num3]

n = len(List)
for i in range(n) :
    for j in range(i+1, n) :
        if List[j] <= List[i] :
            List[i], List[j] = List[j], List[i]

print(List)