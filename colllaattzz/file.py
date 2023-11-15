import collatzz
num = int(input('enter any number: '))


while num != 1:
    num = collatzz.collatz(num)
    print(num)