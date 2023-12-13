import util

array = []

user = ''
while user != 'end' :
    user = input('enter a number for the list')
    array.append(user)
array.remove('end')
array = list(map(int, array))



print(util.maximum(array))