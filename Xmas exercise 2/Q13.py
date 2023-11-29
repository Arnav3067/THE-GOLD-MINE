import utility

year = utility.entryCheck("Enter a year number: ", r"^[0-9]{4}$")

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year!")
else :
    print(f"{year} is not a leap year")
