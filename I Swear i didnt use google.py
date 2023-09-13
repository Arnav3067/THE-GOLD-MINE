# TASK 9
import math

#question 1

name = input('enter your name')
last = name[-1]
first = name[0]
if len(name) % 2 == 0 :
    print('there is no middle letter as the lenght is even')
else :
    middle1 = math.floor(len(name)/2)
    print(first+name[middle1]+last)
    
#question 2

name2 = input('enter your name')
if len(name2)%2 == 0 :
    print('there is no middle letter as the lenght is even')
else :
    middle = math.floor(len(name2)/2)
    left = middle-1
    right = middle +1
    print(name2[left]+name2[middle]+name2[right])
    

#question 3

n = input('enter your input 1')
m = input('enter your second input')
if len(n)%2 ==0 :
    mid = len(n)/2
    mid = int(mid)
    print(n[:mid]+m+n[mid:])
else :
    print('cannot replace a middle charecter as the lenght is odd')
    


#question 4

a = input('enter your string1')
b = input('enter your string2')
if len(a)%2 or len(b)%2 == 0 :
    print('both string lengths have to be odd. TRY AGAIN')
    
else :
    firsta = a[0]
    lasta = a[-1]
    firstb = b[0]
    lastb = b[-1]
    middlea = a[math.floor(len(a)/2)]
    middleb = b[math.floor(len(b)/2)]
    print(firsta+firstb+middlea+middleb+lasta+lastb)
    
