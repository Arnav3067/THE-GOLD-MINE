file = open('C:/Users/kotha/OneDrive/Desktop/computer projects/school_work/file reading exercise/shelley.txt', 'r')
full, empty = 0, 0
for line in file :
    # code for question 4
    if line != '\n' :
        full += 1
    else :
        empty += 1
    

print(f'empty lines: {empty}\nfilled lines: {full}')