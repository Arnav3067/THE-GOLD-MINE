array = input("Enter something:").split()
array[:0] = array[-1]
array.pop()

print(array)

