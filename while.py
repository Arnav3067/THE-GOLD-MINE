#while loops challenges
#q1
'''
total = 0
while total<=50 :
    u = input('enter a number')
    u = int(u)
    total = total +u
    print('total is',total)

#q2
u1 = 0
u1 = int(u1)
while True:
    u1 = input('enter a number')
    u1 = int(u1)
    if u1 >5 :
        break
    
print('the last number you entered was more than 5')

    
=
#q3
u2,u3 = input('enter two numbers').split()
u2 = int(u2)
u3 = int(u3)
summ = u2+u3

while True :
    response = input('do you wnat to add another number').lower()
    if response == 'yes' :
        u4 = int(input('enter another number'))
        summ = summ +u4
     else :
        break
    
print('the total is',summ)

#4
g = []

while True :
    n = input('enter a name for to invite to the party')
    g.append(n)
    r = input('do you want more people invited').lower()
    if r == 'yes' :
        continue
    else :
        break
  
print('the total mebers is',len(g))


#q5

compnum = 50
counter = 0
while True :
    res = int(input('guess a number'))
    counter+=1
    if res == 50 :
        break
    else :
        continue
    
print('you won')
    
#q6

uuu = int(input('enter a number between 10 and 20'))
while True :
    if 10 <uuu< 20 :
        print('thanks bruh')
        break
    else :
        uuu = int(input('try again'))
       


#q6

num= 10
while num > 0:
    print(f"There are {degroot} green bottles hanging on the wall, {degroot} green bottles on the wall, and if 1 green bottle were to fall")
    num  = num - 1
    while True:
        ua = int(input("how many green bottles are hanging on the wall?\n"))
        if ua == num:
            print(f"There will be {degroot} green bottles hanging on the wall")
            break
        else:
            print("try again")
print("There are no more green bottles left on the wall")

'''