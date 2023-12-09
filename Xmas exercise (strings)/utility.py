import re

def entryCheck(
                 inputMessage : str, 
                 regex : str, 
                 errorMessage="" ,
                 Type="int",
                 ):
    while True:
        Input = input(inputMessage).strip()
        if re.search(regex, Input) :
            if Type == "float" : return float(Input)
            if Type == "int" :return int(Input)
            if Type == "string" or Type == "char" : return Input
        else :
            if not errorMessage :
                pass
            else:
                print(errorMessage, end='...... ')
                
def power(base, exponent) :
    total = 1
    for _ in range(exponent) :
        total *= base
        
    return total

def reverse(Input: str, Type="string") :
    temp = ""
    for i in range(len(Input)-1, -1, -1) :
        temp += Input[i]
        
    return temp


def splat(Input, sep=" ") :
    temp, Temp = "", ""
    InputList = []
    
    for i in Input :
        temp += i
        if i == sep :
            InputList.append(temp.strip())
            temp = ""
        
    for i in range(len(Input)-1, -1, -1):
        Temp += Input[i]
        if Input[i] == sep :
            break
    
    InputList.append(Temp[::-1].strip())
    return InputList


        
            