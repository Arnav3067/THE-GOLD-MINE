import VeryUsefulStuff as vus
import re


def main() :
    words = input("Enter a sentence : ").lower()
    listOfWords = words.split()
    print("""
1. Letter frequency
2. Word frequency
""")

    choice = vus.entryCheck("Enter thy choice : ", r"^[1-2]{1}$", "Invalid Input: Try again")
    

    def InitiateLetterFrequency() :
        target = vus.entryCheck("\nEnter the target letter : ", r"[a-z-A-Z]{1}", Type="string").lower()
        print(f"The frequeny of the letter {target} is {GetFrequencyOfElement(words, target)}")

    def InitiateWordFrequency() :
        target = vus.entryCheck("\nEnter the target letter : ", r"^[a-z-A-Z]+$", Type="string").lower()
        print(f"The frequency of the word {target} is {GetFrequencyOfElement(listOfWords, target)}")

    match choice :
        case 1 : InitiateLetterFrequency()
        case 2 : InitiateWordFrequency()

def GetFrequencyDict(List) :
    dictionary = {}
    for element in List :
        temp = GetFrequencyOfElement(List, element)
        dictionary[temp] =  element # this was on purpose because python will just remove the repeated keys

    return dict(sorted(dictionary.items(), reverse=True))




def GetFrequencyOfElement(words, target) :
    counter = 0
    for i in words :
        if (i == target) :
            counter += 1
    return counter


def Book() :
    book = open("book.txt", 'r')
    wordList = []
    
    # makes a filtered list of all words
    for line in book :
        for word in line.split():
            if(not word.isalpha()) :
                word = WordFilter(word)
            wordList.append(word)

    wordFrequency = GetFrequencyDict(wordList)
    
    counter = 0
    for key,value in wordFrequency.items() :
        print(f"{key}   {value}")
        counter += 1
        if (counter > 10) :
            break



def WordFilter(word: str) :
    for char in word :
        if (not char.isalpha()) :
            word = word.replace(char, "")
    return word


Book()
# main()
