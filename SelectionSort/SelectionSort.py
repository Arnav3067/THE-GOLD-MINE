
def Min(numbers) :
    minimum = numbers[0]
    for i in numbers :
        if (minimum > i) : minimum = i
    return minimum


def SwapElements(List, pos1, pos2):
    temp = List[pos1]
    List[pos1] = List[pos2]
    List[pos2] = temp
    return List



def main():
        
    List = input("Enter thy numbers : ").split()
    List = list(map(int, List))
    passes = len(List) - 1

    for i in range(passes) :
        marker = i
        
        numbersOnRight = List[marker + 1::]
        print(numbersOnRight)
        minimum = Min(numbersOnRight)
        minimumIndex = List.index(minimum)

        if (List[marker] > minimum) : List = SwapElements(List, marker, minimumIndex)

    print(List)
main()