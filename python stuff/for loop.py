'''

n = input('enter yoyur name')
for i in [1,2,3] :
    print(n)

n,num = input('enter yoyur name and a natural number').split()
num = int(num)
for i in range(num) :
    print(n)
    


n,num2 = input('enter yoyur name and two natural numbers').split()
num2 = int(num2)
l = len(n)
for i in range(num2) :
    for j in range(l) :
        print(n[j])
        



num3 = int(input('enter a number between 1 and 12'))
for i in [1,2,3,4,5,6,7,8,9,10] :
    t = num3*i
    print(num3,'x',i,'=',t)
    



num4 = input('enter a number bellow 50\n')
num4 = int(num4)
nn = num4
r = 50-num4
x = 50
print(50)
for i in range(r) :
     x = x-1
     if x == num4 :
         break
     else :
         print(x)

print(nn)




user,nnn = input('enter your name and a number').split()
nnn = int(nnn)
if nnn<10 :
    for k in range(nnn) :
        print(user)
else :
    for k2 in range(3) :
        print('too high')
    
'''

total = 0
for i in range(5):
    ux = int(input('enter a number'))
    uuu = input('do you want', ux, 'to be in the total ?')
    uuu.lower()
    if uuu == 'yes' :
        total = total +ux
    
print('this is the total :',total)
        