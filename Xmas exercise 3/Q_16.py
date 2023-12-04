import utility

n = utility.entryCheck("Enter a number n: ", r"^[1-9]+$")
numbers = []
for _ in range(n) :
    numbers.append(utility.entryCheck("Enter a number: ",
                                      r"^[0-9]+$", 
                                      "TypeError: Invalid entry, number cannot be negative"))

total = sum(list(map(int, numbers)))
mean = total/len(numbers)

print(f'{" + ".join(list(map(str, numbers)))} = {total}')
print(f"the mean is: {mean}")