import utility

char = utility.entryCheck("Enter a character: ", r"^[a-zA-Z0-9!@#$%^&*]$", Type="char")

if char.lower() in "aeiou" :
    print("its a vowel!")
else :
    print("its a consonant")