
import VeryUsefulStuff as vus

menu = """
0.Exit
1.Create a new file
2.Display a file
3.Add a new item to an existing file"""

files = {}

def main() :
    print(menu)
    choice = vus.entryCheck("\nEnter thy choice : ", r"^[0-3]{1}$", "Invalid entry: try again")
    
    def InitFileCreation() :
        fileName = ""
        while (fileName in files.keys()) or (fileName == "") :
            fileName = input("Enter a file name and extension (without spaces!) : ")
        CreateFile(fileName)
        
    def InitFileDisplay() :
        Input = GetUserFileChoice()
        DisplayFile(files[Input])
 
    def InitElementAddition() :
        Input = GetUserFileChoice()
        element = input("Enter the element you want to add: ")
        AddElementToFile(element, files[Input])

    match choice :
        case 1 : InitFileCreation()
        case 2 : InitFileDisplay()
        case 3 : InitElementAddition()
    
    return choice

def GetUserFileChoice() :
    Input = ""
    print(f"These are the total files at this moment: {' '.join(files.keys())}")
    while Input not in files.keys() :
        Input = input("Enter an existing file name: ")
    return Input

def CreateFile(name) :
    files[name] = open(f"{name}", 'w')


def DisplayFile(file) :
    print(f"--------------- {file.name} ---------------")  
    file = changeFileMode(file, "r") 
    for line in file :
        print(line, end="")
    print(f"-----------------------------------------")


def AddElementToFile(element, file) :
    file = changeFileMode(file, "a")
    file.write(f"{element}\n")

def changeFileMode(file, mode) :
    file.close()
    file = open(file.name, mode)
    return file

if __name__ == "__main__" :
    while main() != 0 :
        pass
    for file in files.values() :
        file.close()

