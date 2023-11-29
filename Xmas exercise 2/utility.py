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
                print(errorMessage, end='......')