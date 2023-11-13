def greatestOfAll1(num1,num2,num3):

    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3 :
        return num2
    else:
        return num3

def greatestOfAll2(num1,num2,num3):
    if num1 > num2 :
        if num1 > num3:
           return num1
        else :
           return num3
    else :
        if num2 > num3 :
           return num2
        else :
           return num3
        
def greatestOfAll3(num1, num2, num3):
    maximum = num1
    if maximum < num2:
        maximum = num2
    if maximum < num3 :
        maximum = num3
    return maximum