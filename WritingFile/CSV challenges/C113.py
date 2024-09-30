
import C111 as c
from C112 import *

dataAmount = int(input("Enter the amount new book data : "))
counter = 0
while counter < dataAmount :
    userDataDict = GetUserDataDict()
    c.writer.writerow(userDataDict)
    counter += 1

author = input("Enter an author : ").strip().lower()


def changeFileMode(file, mode) :
    file.close()
    file = open(file.name, mode)
    return file


c.books = changeFileMode(c.books, "r")
for i in c.books :
    print(i.split(','))


