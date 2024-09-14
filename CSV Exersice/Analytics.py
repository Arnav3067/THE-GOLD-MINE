import VeryUsefulStuff as vus

menu = """
1.Median
2.Mode
3.Mean
4.Max 5 numbers
5.Min 5 numbers
0.Exit
6.Frequency			Enter your choice: """


def main() :
    ListFile = open("C:\\Users\\22AKothari.ACC\\Desktop\\Computer science\\Analytics\\Analytics test file.txt", 'r')
    List = []
    for i in ListFile :
        List = i.split()
    List = list(map(int, List))
    
    choice = vus.entryCheck(menu, r"^[0-6]{1}$", Type="int")
    
    match choice :
        case 1 : print(f"The median is : {GetMedian(List)} ")
        case 2 : print(f"The Mode is : {GetMode(List)}" )
        case 3 : print(f"The Mean is : {GetMean(List)}")
        case 4 : print(f"The top 5 numbers are : {GetTop5(List)}")
        case 5 : print(f"The low 5 numbers are : {GetLow5(List)}")
        case 6 : print(f"The Frequency is (num, freq) : {GetFrequency(List)}")
        
    return choice
    
    

def GetMean(List) :
    return sum(List)/len(List)

def GetMedian(List) :
    List.sort()
    mid = (0 + (len(List) - 1))//2
    return List[mid]

def GetLow5(List) :
    top5 = []
    List.sort()
    if (len(List) < 5) :
        return List
    
    for i in range(5) :
        top5.append(List[i])
    return top5

def GetTop5(List) :
    low5 = []
    List.sort()
    List.reverse()
    if (len(List) < 5) :
        return List
    
    for i in range(5) :
        low5.append(List[i])
    
    return low5

def GetMode(List) :
    
    maxOccurance = max(list(map(List.count, List)))
    
    for i in range (len(List)) :
        counter = 0
        for j in range(len(List)) :
            if (List[j] == List[i]) :
                counter += 1
        if (counter == maxOccurance) :
            return List[i]
        
def GetFrequency(List) :
    
    frequency = []
    
    for i in range (len(List)) :
        counter = 0
        for j in range(len(List)) :
            if (List[j] == List[i]) :
                counter += 1
        frequency.append((i, counter))
    
    return frequency
            
            
                

    
if __name__ == "__main__" :
    while main() != 0 :
        pass