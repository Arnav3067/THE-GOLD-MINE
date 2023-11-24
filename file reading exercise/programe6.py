name = input('enter the file path: ')

file =  open(f'{name}', 'r')
counter, summ = 0,0
for line in file :
    if not line == '\n' :
        line = int(line)
        summ += line
        counter +=1
print(summ/counter)