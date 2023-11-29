import utility 

number = utility.entryCheck("Enter a number: ", "^[1-7]$", errorMessage="ValueError: number is not in range [1-7]")

daysWithNumbers = {

    1 : "Sunday",
    2 : "Monday",
    3 : "tuesday",
    4 : "wednesday",
    5 : "Thursday",
    6 : "friday",
    7 : "saturday"

}

print(f"The day is {daysWithNumbers[number]}")