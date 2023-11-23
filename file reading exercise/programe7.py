name= input('enter the file name: ')
summ = 0
counter = 0
file = open(f'C:/Users/kotha/OneDrive/Desktop/computer projects/school_work/file reading exercise/{name}','r')

for line in file:
    if line != '\n' : 
        summ += int(line)
        counter += 1
asnw = summ/counter

print(asnw, 'is the mean')
        