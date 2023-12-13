import util

stringArray = util.splat(util.entryCheck("Enter a string: ", Type="string"))
backup = stringArray.copy()


victim = ""
while victim not in stringArray :
    victim = util.entryCheck("Enter the word that you want to delete: ", Type="string")
   
for i, element in enumerate(stringArray):
    if victim == element :
        word = stringArray.pop(i)
        
ogString = " ".join(backup)      
newString = " ".join(stringArray)

charsInWords = len(word)
charsInNewString = len(newString)
charsInOgString = len(ogString)


print(f'''
og string: {ogString}   chars = {charsInOgString}
new string: {newString} chars = {charsInNewString}
word removed: {word}    chars = {charsInWords}
      ''')