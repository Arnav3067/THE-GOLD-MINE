import utility
total = 0
for i in range(1, utility.entryCheck("Enter a number n: ", r"^[0-9]+$") + 1) :
    total += 1/i

print(f'{total:.2f}')