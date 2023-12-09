import utility

string = utility.entryCheck("Enter a string: ", r"^.+$", Type="string")

if string == utility.reverse(string) :
    print(f"{string} is a Palindrome!")
else :
    print(f"{string} is not a Palindrome!")
    
