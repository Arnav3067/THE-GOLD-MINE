import util

dateArray = util.splat(util.entryCheck("Enter a date in the form mm/dd/yyyy: ", r"^[0-9]{0,2}\/[0-9]{0,2}\/[0-9]{0,4}$", Type="string"),
                       sep="/")
month, day, year = list(map(int, dateArray))

print(f"{util.Months[month]}, {day}, {year}")



