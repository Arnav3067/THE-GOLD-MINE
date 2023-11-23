file = open('C:/Users/kotha/OneDrive/Desktop/computer projects/school_work/file reading exercise/shelley.txt', 'r')

for line in file:
    newList = line.split()
    for i in newList :
        print(i[0].upper() + i[1::], end=' ')