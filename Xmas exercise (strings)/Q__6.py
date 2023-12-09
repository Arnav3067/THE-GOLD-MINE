from utility import *

stringList = splat(entryCheck("Enter a string: ", r"^.+$", Type="string"))

for i in stringList :
    print(i[0].upper()+".", end=" ")
    
