import VeryUsefulStuff as vus

sep = ", "

file = open("Passwords.csv", 'a')
header = f"UserID{sep}Passwords\n"
# file.write(header) # header

menu = """
1. Create a new user id
2. Change a passwords
3. Display all user Id's
0. Exit
"""

    

def _main() :


    print(menu)
    choice = vus.entryCheck("Enter your choice: ", r"^[0-3]{1}$")

    def initIDCreation(data) :
        while True:
            newId = input("Enter a new user ID : ")
            data = changeFileMode(data, 'r')
            if CheckUserId(data, newId):
                print("ID Exists ", end="")
            else :
                break
        CreateUserID(data, newId, GetNewPassword())
        
    def initPasswordReplacement(data) :
        while True:
            userId = input("Enter a user ID : ")
            data = changeFileMode(data, 'r')
            if CheckUserId(data, userId):
                break
        ChangePasswordOf(data, userId)


    match choice :
        case 1 : initIDCreation(file)
        case 2 : initPasswordReplacement(file)
        case 3 : DisplayFile(file)
    
    return choice

def DisplayFile(data):
    dataList = GetDataList(data)
    for line in dataList :
        print(sep.join(line), end="")

def ChangePasswordOf(data, id):
    data = changeFileMode(data, 'r')
    index = 0
    for line in data :
        lineList = GetListFromLine(line)
        if id in lineList :
            lineList[1] = GetNewPassword()
            break
        index += 1
    data = changeFileMode(data, 'a')
    data.write(sep.join(lineList) + "\n")
    RemoveLine(data, index)
    

def RemoveLine(data , index) :
    dataList = GetDataList(data)
    dataList.remove(dataList[index])
    data = changeFileMode(data, "w")
    data = changeFileMode(data, 'a')
    for line in dataList :
        data.write(sep.join(line))

def GetDataList(data) :
    data = changeFileMode(data, 'r')
    dataList = []
    for line in data :
        dataList.append(line.split(sep))
    return dataList 

def GetListFromLine(line) :
    line = line.replace("\n", "")
    return line.split(sep)

def changeFileMode(file, mode) :
    file.close()
    file = open(file.name, mode)
    return file

# returns true if userId does not exist already
def CheckUserId(data, newId):
    IdExists = False
    for line in data :
        lineList = GetListFromLine(line)
        if newId in lineList  or newId == "":
            IdExists = True
    return IdExists


def CreateUserID(data, Id, password) :
    data = changeFileMode(data, 'a')
    data.write(f"{Id}{sep}{password}\n")


def GetNewPassword() :
    password = ""
    while CheckPassword(password) == False :
        password = input("Enter a password: ")
    return password
    
# returns true if the password is valid
def CheckPassword(password : str):
    checks = []

    if len(password) >= 8 :
        checks.append(True)

    upper, lower, special, number = 0,0,0,0
    for char in password :
        if char.isupper() : 
            upper += 1
            continue
        if char.islower() : 
            lower += 1
            continue
        if char.isdigit() : 
            number += 1
            continue
        if (char.isalpha() != True) : special += 1

    if upper >= 2 and lower >= 2 and number >= 2 and special >= 1:
        checks.append(True)
    
    return len(checks) == 2

while _main() != 0 : pass

file.close()