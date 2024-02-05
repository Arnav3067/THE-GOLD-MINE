#1
'''

first, last = input('enetr your full name').split()
print(len(first))
print(len(last))
print(f'your full name is : {first} {last}')

#2
sub = []
sub.extend(input('enetr your school subject'))
count = 0
sub = str(sub)
sub = sub.replace(',', '')
sub = sub.replace("'", '')
sub = sub.replace(' ', '-')
print(sub)


#3

text = 'the ridiculous and the sub lime'
print(text)

start, end= input('enter a starting point and an ending point in the order').split()
start = int(start)
end = int(end)

print(text[start : end])


#4
running = True
while running :
    string = input('enter a texxt inn upper case')
    if  string.isupper() :
        print('true')
        running = False
        
    

#5

post = input('enetr your postcode')
print(post[0:2].upper())

#6
counter = 0
name  = input('enter your name')

for i in range(len(name)) :
    if name[i] == 'a' or name[i] ==  'e' or name[i] ==  'i' or name[i] == 'u' or name[i] == 'o' :
        counter += 1
        
print(counter)



#7

pasword1 = input('enetr a password')
pasword2 = input('enter the password again')

if pasword1 == pasword2 :
    print('thank you')
if pasword1.isupper() :
    if pasowrd2.islower() :
        print('they have to be in the same case')
else :
    if pasword2.isupper() :
        print('they have to be the same case')
        

'''
#8

enter = input('enter a word')
print(enter[::-1])

