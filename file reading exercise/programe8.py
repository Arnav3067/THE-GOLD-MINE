file = open('C:/Users/kotha/OneDrive/Desktop/computer projects/school_work/file reading exercise/shelley.txt','r')
counter = 0
for line in file:
    for letter in line:
        if letter != '\n' :
            counter += 1

print(counter)