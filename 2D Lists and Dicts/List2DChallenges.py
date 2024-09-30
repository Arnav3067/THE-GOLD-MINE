import VeryUsefulStuff as vus

List2D : list[list] = [[2,5,8], [3,7,4], [1,6,9], [4,2,0]]

def _main() :

    # challenge 1
    row = vus.entryCheck("Enter a row number: [0-3]: ", r"^[0-3]{1}$", "Row does not exists")
    column = vus.entryCheck("Enter a column number: [0-2]: ", r"^[0-2]{1}$", "Row does not exists")
    DisplayElement(row, column, List2D)

    # challenge 2
    row = vus.entryCheck("\nEnter a row you want displayed: [0-3]: ", r"^[0-3]{1}$", "Row does not exists")
    DisplayRow(row, List2D)
    newValue = vus.entryCheck("Enter a new value: ", r"^[0-9]+$")
    AddToRow(row, newValue, List2D)
    DisplayRow(row, List2D)

    # challenge 3
    row = vus.entryCheck("\nEnter a row you want displayed: [0-3]: ", r"^[0-3]{1}$", "Row does not exists")
    DisplayRow(row, List2D)
    column = vus.entryCheck("Enter a column number: [0-2]: ", r"^[0-2]{1}$", "Row does not exists")
    DisplayElement(row,column, List2D)
    choice = vus.entryCheck("Do you want to change this value? [Y/N]: ", r"^[ynYN]{1}", Type="string")
    if (choice.lower() == "y") :
        value = vus.entryCheck("Enter the new value: ", r"^[0-9]+$")
        ChangeElement(row, column, value, List2D)
    DisplayRow(row, List2D)


def ChangeElement(row, column, value, dataSet):
    dataSet[row][column] = value

def DisplayElement(row, column, dataSet):
    print(dataSet[row][column])

def DisplayRow(row, dataSet) :
    print(dataSet[row])

def AddToRow(row, element, dataSet):
    dataSet[row].append(element)
    



if __name__ == "__main__" :
    _main()