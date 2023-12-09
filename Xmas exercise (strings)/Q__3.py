import utility

string = utility.entryCheck("ENter a string: ", r"^.+$", Type="string")

print(string[-1] + string[1:len(string)-1] + string[0])