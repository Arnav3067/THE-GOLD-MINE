import utility 

string = utility.entryCheck("Enter a string: ", r"^.+$", Type="string")

print(string[1:len(string)] + string[0])
