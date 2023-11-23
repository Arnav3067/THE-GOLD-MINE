file = open('C:/Users/kotha/OneDrive/Desktop/computer projects/school_work/file reading exercise/numbers.txt', 'r')
total = 0
for line in file :
    if line != '\n': total += int(line) 
    print(total) # code for question 2
# print(total) , code for part 1
