words = ['apple', 'bannana', 'cherry']
s = [' hello', ' python', ' world ']
cel = [0, 20, 37, 100]

def GetFirstLetter(word) :
    return word[0]


def GetUpper(word) : return word.upper()

def FilterWord(word : str) : return word.strip()

def ConvertToFarh(c) :
     return (c*9/5) + 32
        
result = list(map(ConvertToFarh, cel))
print(result)