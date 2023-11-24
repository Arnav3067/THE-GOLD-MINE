file  = open('C:/Users/22AKothari.ACC/Downloads/shelley.txt','r')
newList =[]

for line in file:
    newList.append(line)

start = int(input('enter a start range'))
end  = int(input('enter a an ending range'))

for i in range(start-1,end) :
    print(newList[i], end='')