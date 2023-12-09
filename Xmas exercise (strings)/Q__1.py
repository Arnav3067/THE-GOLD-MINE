import utility

string = utility.entryCheck("Enter a string: ", r"^[a-zA-z !@#$%^&*]+$", Type="string")
count = 0
for i in string.lower():
    if i in ["a", "e", "i", "o", "u"] :
        count += 1
        
print(f"The number of vowels: {count}")