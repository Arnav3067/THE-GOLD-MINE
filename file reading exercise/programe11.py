file = open('C:/Users/kotha/OneDrive/Desktop/computer projects/school_work/file reading exercise/feedback.txt', 'r')
p,n,total = 0,0,0
for line in file :
    if line[0].lower() == 'p' :
        p += 1
    else :
        n += 1
    total += 1

print(f'positive: {p} negative: {n} total: {total}')