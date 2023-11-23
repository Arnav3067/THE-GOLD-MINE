file = open('C:/Users/kotha/OneDrive/Desktop/computer projects/school_work/file reading exercise/shelley.txt','r')

for line in file :
    storage = line.split()
    if len(storage) > 8 :
        print(line.strip())