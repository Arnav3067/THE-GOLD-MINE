import re


Months = {
    1: "January",
    2: "february",
    3: "March",
    4: "April", 
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "september",
    10: "october",
    11: "november",
    12: "december"
}

def entryCheck(
                 inputMessage : str, 
                 regex = r".*", 
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
    if Type == 'string':
        temp = ""
        for i in range(len(Input)-1, -1, -1) :
            temp += Input[i]
            
        return temp
    elif Type == 'list' :
        array = []
        for i in range(len(Input)-1, -1,-1) :
            array.append(Input[i])
        return array
        


def splat(Input, sep=" ") :
    temp, Temp = "", ""
    InputList = []
    
    for i in Input :
        temp += i
        if i == sep :
            InputList.append(temp.strip(sep))
            temp = ""
        
    for i in range(len(Input)-1, -1, -1):
        Temp += Input[i]
        if Input[i] == sep :
            break
    
    InputList.append(Temp[::-1].strip(sep))
    return InputList

def maximum(array) :
    for i in array :
        m = i
        for j in array :
            if m < j :
                m = j
            
    return m

        
            