import C111 as c

def GetUserDataDict() :
    userData = input("Enter your data for a new book : ").split()
    userDataDict = {}
    for i in range(len(userData)) :
        userDataDict[c.fieldNames[i]] = userData[i]
    return userDataDict

if __name__ == "__main__" :
    c.writer.writerow(GetUserDataDict())
