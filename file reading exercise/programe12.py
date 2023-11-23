file = open('C:/Users/kotha/OneDrive/Desktop/computer projects/school_work/file reading exercise/badSpelling.txt', 'r')

for line in file:
    newList = line.split()
    for i in newList :
        if i[-1].isdigit():
            print(i)