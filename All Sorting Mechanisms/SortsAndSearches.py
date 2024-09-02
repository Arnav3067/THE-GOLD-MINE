import VeryUsefulStuff as vus

menu = """

1.Bubble Sort
2.Binary Search
3.Linear Search
4.Selection Sort    
0.Exit              Enter your choice : """



List = vus.entryCheck("Enter the Numbers (With Spaces): ", regex= r"^([0-9]+ *)+$", Type="string").split()


def main(List) :

    def InitBinarySearch() :
        target = vus.entryCheck("\nEnter the target value: ", r"^[0-9]+$", Type="int")
        print(f"The target value {target} is at index : {BinarySearch(List, target)}")

    def InitLinearSearch() :
        target = vus.entryCheck("\nEnter the target value: ", r"^[0-9]+$", Type="int")
        print(f"The target value {target} is at index : {LinearSearch(List, target)}")

    choice = vus.entryCheck(menu, r"^[0-4]{1}$", errorMessage="Invalid entry: dude seriously?", Type="int")

    match choice :
        case 1 : print(f"\nThe sorted list is : {BubbleSort(List)}")
        case 2 : InitBinarySearch()
        case 3 : InitLinearSearch()
        case 4 : print(f"\nThe sorted List is : {SelectionSort(List)}")



def SwapElements(List, pos1, pos2):
    mem = List[pos1] 
    List[pos1] = List[pos2] 
    List[pos2] = mem
    return List


def BubbleSort(List) :
    passes = len(List) - 1

    for _ in range(passes) : 
        for i in range(len(List) - 1) : 
            a, b= List[i], List[i+1]
            if (a > b) : 
                SwapElements(List, i, i+1) 

    return List

def SelectionSort(List) :
    passes = len(List) - 1

    for i in range(passes) :
        marker = i
        numbersOnRight = List[marker + 1::]
        minimum = Min(numbersOnRight)
        minimumIndex = List.index(minimum)
        if (List[marker] > minimum) : List = SwapElements(List, marker, minimumIndex)
    return List

def LinearSearch(List, target) :

    for i in range(len(List)) :

        if (List[i] == target) :
            return i
            

def Min(numbers) :
    minimum = numbers[0]
    for i in numbers :
        if (minimum > i) : minimum = i
    return minimum


def BinarySearch(List, target) :

    low = 0
    high = len(List) - 1
    List = BubbleSort(List)

    while low <= high:
        mid = (low + high)//2

        if (List[low] == target) : return low
        elif (List[high] == target) : return high
        elif (List[mid] == target) : return mid
        else :
            if (List[mid] < target) : 
                low = mid + 1
            else: 
                high = mid - 1

    return -1


if __name__ == "__main__" :

    while main(List) != 0 :
        pass
