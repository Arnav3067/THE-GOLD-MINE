'''

suer = input('enytter your name')
lenght = len(suer)
print('this is the leanght of your name',lenght)


first,last = input('enter your full name').split()
full = first+last
l = len(full)
print('your full name is',first,last,'and the lenght is',l)
                                                 

f,lastt = input('enter your full name(in lower case)').split()
a = f[0].upper()
b = lastt[0].upper()
print(a+f[1:],b+lastt[1:])


rhyme = input('enter the rhymr')
start,end = input('enetr the strat and the end number').split()
start = int(start)
end = int(end)
start = start-1
end = end-1
print(rhyme[start:end])



u = input('enter anything')
u = u.upper()
print(u)



us = input('enter your first name')
le = len(us)
if le < 5 :
    s = input('enter ypur sir name')
    fl = us+s
    print('your full name is',fl.upper())
    
else :
    print('your first name is',us.lower())
    


use = input('enetr anything').lower()

if use[0] == 'a' :
    print(use+'way')
elif use[0] == 'e' :
    print(use+'way')
elif use[0] == 'i' :
    print(use+'way')
elif use[0] == 'o' :
    print(use+'way')
elif use[0] == 'u' :
    print(use+'way')
else :
    print(use[1:]+use[0]+'ay')
    
    
    '''
    