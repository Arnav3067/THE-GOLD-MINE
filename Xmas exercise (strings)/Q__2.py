import utility

upper, lower, space, digits, weird = 0,0,0,0,0

string = utility.entryCheck("Enter a string: ", r"^.+$", Type="string")

for i in string:
    if i.isdigit() :
        digits += 1
    elif i.isupper() :
        upper += 1
    elif i.islower() :
        lower += 1
    elif i == " ":
        space += 1
    else :
        weird += 1
        
print(f'''
upper: {upper}
lower: {lower}
digits: {digits}
spaces: {space}
weird: {weird}
      ''')