import utility

print(utility.power(utility.entryCheck("Enter the base: ", r"^-?[0-9]+$"),
            utility.entryCheck("Enter the exponent: ", r"^-?[0-9]+$")))