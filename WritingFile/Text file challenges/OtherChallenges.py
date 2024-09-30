

numbers = open("Numbers.txt", 'w')
names = open("Names.txt", 'r')

# challenge 105
numbers.write("1, 2, 3, 4, 5")

# challenge 106
numbers.write("Po\nJudgement\nMoveIt\nCurry\n")

# Challenge 107
for line in names :
    print(line, end="")

# challenge 108
names.close()
names = open("Names.txt", 'a')
username = input("Enter a name")
names.write(username)
names.write("\n")

# challenge 110
names.close()
names = open("Names.txt", 'r')

for line in names:
    print(names)
userInput = input("Enter the name to be eliminated")

newSet = ""

for line in names :
    if line != userInput :
        newSet += line

newfile = open("Numbers2.txt", 'w')
newfile.write(newSet)


