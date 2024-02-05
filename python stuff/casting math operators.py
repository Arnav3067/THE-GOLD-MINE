'''
Exercise 3
MB = 1
CoC = float(1.5)
BoC = float(0.8)
CoT = 2
SP = float(3.50)
total=(MB*5)+(CoC*4)+(BoC*3)+(CoT*2)+SP
print(total)

Exercise 4
number1 = int(input("Enter first number:\n"))
number2 = int(input("Enter second number:\n"))
ans= number1+number2
print("The answer is:", ans)

Exercise 5
AmericaTemp = float(input("Insert your temperature in fahrenheit\n"))
CorrectTemp=float((AmericaTemp-32)*(5/9))
print("The temperature is:", CorrectTemp)

Exercise 6
dd=int(input("What day of the month were you born on?\n"))
TM=int(input("What month were you born in? (enter in numbers please)\n"))
y1=int(input("What year were you born in?\n"))
y=y1%100
c=int((y1-y)/100)
print(c, y)
if 0<TM<3:
    mm=TM+12
    y=y-1
else:
    if 2<TM<13:
        mm=TM
top=13*(mm+1)
a=top//5
b=float(y//4)
C=c//4
d=2*c
w=(dd+a+y+b+C-d)%7
print("You were born on the", w, "day of the week")
print(top, mm, a, b, C, d)
'''
