import utility
total = 1
for i in range(1, utility.entryCheck("Enter a number n for n! : ", "^[0-9]+$") + 1) :
    total *= i
print(total)