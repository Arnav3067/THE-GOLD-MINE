import util

number = util.entryCheck("Enter a 10 digit number:", r"^[1-9][0-9]{9}$", Type="string")
numberArray = []

for i in number :
    numberArray.append(i)
    
numberArray = list(map(int, numberArray))

for i, num in enumerate(numberArray) :
    
    if num % 2 != 0 :
        print(i, end=" ")
