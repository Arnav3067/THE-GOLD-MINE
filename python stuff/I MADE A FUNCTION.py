import random
def arnav(x):
    x = abs(x)
    return(x)
    
    

'''
#q1

m = random.randint(1,100)
print(m)


#q2
fruits = ['banana','apple','ladyfinger','strawberry','kiwi']
r = random.choice(fruits)
print(r)


#q3

raw = random.choice(['h','t'])

user= input('heads or tails(h/t)')
while True :
    
    if user == raw :
        
        print('you win')
        break
    else :
        print('you lose')
        user = input('enetr again')
        
        
print('thge computer chose',raw)

#q4

num = random.randint(1,5)
us = int(input('guess a number closer to mine.'))
while True :
    if us == num :
        print('you guessed correctly\nthe number was',num)
        break
    else :
        a = arnav(us-num)
        if a<num :
            print('too low')
            us = int(input('enter again'))
            
        else :
            print('too high')
            us = int(input('enter again'))
            

#q5 +q6

num2 = random.randint(1,10)
uss = int(input('guess a number closer to mine.'))
while True :
    if uss == num2 :
        print('you guessed correctly\nthe number was',num)
        break
    else :
        a = arnav(uss-num2)
        if a<num2 :
            print('too low')
            uss = int(input('enter again'))
            
        else :
            print('too high')
            uss = int(input('enter again'))
            
            


#q7

s = 0
for i in range(5) :
    n1 = random.randint(0,1000)
    n2 = random.randint(0,1000)
    summ  = n1 * n2
    use = int(input(f'what is {n1} x {n2} = '))
    if use == summ :
        s = s + 1
         
         
print('your final score is ',s)

'''

#q8

colurs = ['red','blue','orange','black','gray']
ran = random.choice(colurs)

userr = input('guess my colour').lower()

while True :
    if userr == ran :
        print('you guessed it right')
        break
    elif ran == colurs[0] :
        userr = input('your face is RED\nenter again').lower()
    elif ran == colurs[1] :
        userr =input('your face is BLUE\nenter again').lower()
    elif ran == colurs[2] :
        userr = input('you should just keep peelling your ORANGE\nenter again').lower()
    elif ran == colurs[3] :
        userr = input('you are turnimg BLACK\n enter again').lower()
    elif ran == colurs[4] :
        userr = input('the answer is GRAY in coulur')
 
            



