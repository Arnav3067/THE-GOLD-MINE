
import random

# ch 118

def userInput():

    num = int(input('enter a number: '))
    return num

def fromOneToN(num):

    for i in range(1,num+1):
        print(i, end=' ')

num = userInput()
fromOneToN(num)


# ch 119

def randomNumber():

    numA, numB = input('\nenter a low number and high number: ').split()
    numA = int(numA)
    numB = int(numB)

    return random.randint(numA, numB)


def userNumber():

    return int(input('i am thinking of a  number....... guess what it is?  '))


def guessingGame(man, comp):

    while True:

        if man > comp :
            print('too high')
            man = userNumber()
        elif man < comp :
            print('too low')
            man = userNumber()
        else :
            print('correct you win!')
            break
            
comp_num = randomNumber()
num = userNumber()
guessingGame(num, comp_num)


# ch 120

def displayMenu():
    oneOrTwo = 0
    while(oneOrTwo != 1 and oneOrTwo != 2):
        oneOrTwo = int(input('1) Addition\n2) Subtraction\nEnter 1 or 2:\n'))
        if not oneOrTwo in [1, 2]:
            print('please enter a valid number!\n')

    return oneOrTwo

def  addOrSubtract(oneOrTwo):

    if oneOrTwo == 1:
        numA = random.randint(5, 20)
        numB = random.randint(5, 20)
        correctAnswer = numA + numB
        userAnswer = int(input(f'solve this expression:    {numA} + {numB} = '))
        rightOrWrong(correctAnswer, userAnswer)
    else :
        numA = random.randint(25, 50)
        numB = random.randint(1, 25)
        correctAnswer = numA - numB
        userAnswer = int(input(f'solve this expression:    {numA} - {numB} = '))
        rightOrWrong(correctAnswer, userAnswer)

def rightOrWrong(correctAnswer , userAnswer):

    if correctAnswer == userAnswer :
        print('correct!')
        exit()
    else:
        print('incorrect!')


choice = displayMenu()
addOrSubtract(choice)


# ch 121

names = ['Doremon', 'shinChan', 'pikachu']

def menu():
    choice = 0
    while(choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6):

        choice = int(input('''
                        1) View all names
                        2) Add a name
                        3) change a name
                        4) delete a name
                        5) reset the list
                        6) Exit
                        Enter 1, 2, 3, 4 or 5:
                        '''))
        if not choice in [1, 2, 3, 4, 5, 6]:
            print('Please enter a valid number! ')
        elif choice == 6 :
            print(f'Thank you for visiting!!! your final list of names is:   {", ".join(names)}')
            exit()
    return choice

def addName():
    name = input('enter a name you want to add: ')
    names.append(name)
    return names

def changeName():
    print(f'this is the current list of names {names}')
    Name_to_be_changed = input('Enter the Exact name you want to change: ')
    changingName = input('Enter the new name: ')
    index_CN = names.index(Name_to_be_changed)
    names[index_CN] = changingName
    return names

def deleteName():
    print(f'This is the current list of names {names}')
    Name_to_be_deleted = input('Enter the exact to be deleted: ')
    names.remove(Name_to_be_deleted)
    return names


while True:

    option = menu()
    if option == 2:
        names = addName()
    elif option == 1:
        print(names) if len(names) != 0 else print('There are no names in this list (to add enter 2)')
    elif option == 3:
        names = changeName()
    elif option == 4:
        names = deleteName()
    else:
        names.clear()
