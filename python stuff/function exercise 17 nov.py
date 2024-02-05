
#q1
def sumOfLists(numbers) :
    return sum(numbers)
#q2
def multiplyList(numbers) :
    product = 1
    for i in numbers :
        product *= i
    return product

#q3
def reverseString(sentence) :
    return sentence[::-1]
#q4
def factorial(number) :
    product = 1
    for i in range(1,number+1) :
        product *= i
    return product
#q5
def inRange(start, end, number) :
    if start < number < end :
        return 'inside the range'
    else :
        return 'not inside the range'
    
#q6  
def upperLowercounter(sentence) :
    lowerCounter = 0
    upperCounter = 0
    for letter in sentence :
        if letter.isupper() :
            upperCounter += 1
        else :
            lowerCounter += 1
    return f'no. of lower cased letters is: {lowerCounter}', f'no. of upper cased letters is: {upperCounter}'


#q7
def upperLowercounter(array) :
    newList = []
    for i in array :
        if not i in newList :
            newList.append(i)
    return newList


#q8
def isPrime(number) :
    counter = 0
    for i in range(1,number+1) :
        temp = number % i
        if temp == 0 :
            counter += 1
    if counter == 2 :
        return True
    else :
        return False
    
# q9
def evenfilter(numbers) :
    even =[]
    for i in numbers :
        if not i%2 :
            even.append(i)
    return even

