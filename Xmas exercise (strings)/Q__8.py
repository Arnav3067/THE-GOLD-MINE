import utility

new = ""
backup = string = utility.entryCheck("Enter a string: ", r"^.+$", Type="string")

print(string)
while new != backup :
    new = string[1:len(string)] + string[0]
    print(new)
    string = new
    