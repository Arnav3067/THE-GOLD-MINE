file = open('C:/Users/kotha/OneDrive/Desktop/computer projects/school_work/file reading exercise/shelley.txt','r')
newList = []
for line in file:
    newList.append(line)

print(''.join(newList[::-1]))