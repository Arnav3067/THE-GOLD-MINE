import Analytics as a
import VeryUsefulStuff as vus

def GetDataList(file) :
    ListOfLines = []

    for line in file :
        line = line.strip()
        line = line.split(',')
        if (line[3] != '') :
            line = list(map(float, line))
            ListOfLines.append(line)
            
    return ListOfLines

file = open("Exercise.csv", "r")
header = file.readline()
data = GetDataList(file)



def main() :
    ListOfDurations = GetFilteredListOfDurations()
    print(f"\nHere are the possble session duration types you can enter : {', '.join(list(map(str, ListOfDurations)))}")
    userDuration = 0
    while True:
        userDuration = float(input("Enter your seession duration: "))
        if (userDuration not in ListOfDurations):
            print("Invalid Entry: session type not found....")
        else :
            break
    
    userAverageCalorie = vus.entryCheck("Enter your average calories for your duration type (decimal value): ", r"^[0-9]+\.[0-9]+$", Type="float")
    Part4UserInteraction(userDuration, userAverageCalorie)

def Part3() :
    duration = 60
    List = GetTop20Low20Average(duration)
    total = GetAverageCalories(duration)
    print(f"The percentage diff between Low20 and Top20 of {duration} duration type is : {GetPercentageDifference(List[0], List[1], total):.2f}")
    
def Part4UserInteraction(duration, calories) :
    computedAverageCalories = GetAverageCalories(duration)
    
    comparedValue = computedAverageCalories - calories
    if comparedValue > 0 :
        print(f"Your average calorie ({calories}) is {comparedValue:.2f} units smaller than the computed average calorie ({computedAverageCalories:2f})")
    elif comparedValue < 0 :
        print(f"Your average calorie ({calories}) is {abs(comparedValue):.2f} units larger than the computed average calorie ({computedAverageCalories:.2f})")
    else :
        print(f"Your average calorie ({calories}) is eaxactly the same as the computed average calorie ({computedAverageCalories:.2f})")


def GetTop20Low20Average(duration) :
    calories = GetCalorieList(duration)
    calories.sort()
    averageCaloriesTop20 = a.GetMean(calories[len(calories) - 20::])
    averageCaloriesLow20 = a.GetMean(calories[0:20])

    return [averageCaloriesLow20, averageCaloriesTop20]    

def GetPercentageDifference(var1, var2, total) :
    return abs(((var1/total) - (var2/total)) * 100)


def Part1() :
    sessionDurations = GetFilteredListOfDurations()
    AverageColoriesForAll = []
    
    for duration in sessionDurations :
         AverageColoriesForAll.append(GetAverageCalories(duration))
        
    print("Durations	Average Calories")
    print("---------	----------------")
    for i in range(len(sessionDurations)) :
        print(f"{sessionDurations[i]}		{AverageColoriesForAll[i]:.2f}")
        
def GetAverageCalories(duration) :
    List = []
    for session in data :
        if (session[0] == duration) :
            List.append(session[3])
    return a.GetMean(List)

def GetCalorieList(duration) :
    List = []
    for session in data :
        if (session[0] == duration) :
            List.append(session[3])
    return List

def GetFilteredListOfDurations() :
        
    filteredList = []
    
    for session in data :
        if (session[0] not in filteredList) :
            filteredList.append(session[0])
        
    return filteredList


main()

