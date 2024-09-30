import VeryUsefulStuff as vus
import List2DChallenges as l

Dict2D = {
    "john" : {"N" : 3056, "S": 8463, "E": 8441, "W" : 2694},
    "tom" : {"N": 4832, "S": 6786, "E": 4737, "W" : 3612},
    "anne" : {"N": 5239, "S": 4802, "E": 5820, "W" : 1859 },
    "fiona" : {"N": 3904, "S": 3645, "E": 8821, "W" : 2451 }
}



def _main():
    
    # # challenge 6
    # name = vus.entryCheck("Enter a name: ", r"^[a-zA-Z]+$", Type="string").lower()
    # region = vus.entryCheck("Enter a region: ", r"^[NSEW]{1}$", Type="string")
    # l.DisplayElement(name, region, Dict2D)
    # name = vus.entryCheck("\nWhose data do you want to change: ", r"^[a-zA-Z]+$", "Row does not exists", "string")
    # l.DisplayRow(name, Dict2D)
    # region = vus.entryCheck("Enter a region:  ", r"^[NSEW]{1}$", "Row does not exists", "string")
    # l.DisplayElement(name,region, Dict2D)
    # value = vus.entryCheck("Enter the new value: ", r"^[0-9]+$")
    # l.ChangeElement(name, region, value, Dict2D)
    # l.DisplayRow(name, Dict2D)


    # challenge 7
    Dict = {}
    for i in range(4):
        name = vus.entryCheck("Enter a name: ", r"^[a-zA-Z]+$", Type="string")
        shoeSize = vus.entryCheck("Enter their shoe size: ", r"^[0-9]+$")
        age = vus.entryCheck("Enter their age: ", r"^[0-9]+$")
        Dict[name] = {"age": age, "shoeSize" : shoeSize}
    
    # name = vus.entryCheck("Enter a name: ", r"^[a-zA-Z]+$", Type="string").lower()
    # l.DisplayRow(name, Dict)

    # # challenge 8
    # for key, value in Dict.items():
    #     print(f"name : {key}    age: {value['age']}")
    name = "" 
    while name not in Dict.keys() :
        name = vus.entryCheck("Enter a name you want to delete: ", r"^[a-zA-Z]+$", Type="string")
    DeleteRow(name, Dict)
    for key in Dict.keys():
        print(key, end="    ")
        l.DisplayRow(key, Dict)
    
def DeleteRow(row, dataSet):
    dataSet.pop(row)

if __name__ == "__main__" :
    _main()