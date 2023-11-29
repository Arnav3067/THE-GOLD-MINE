import utility

calls = utility.entryCheck("Enter the number of calls: ", r"^[0-9]+$")

rate = 200 

if 100 < calls <= 150 :
    if not((150-calls)* 0.60) :
        rate = 230
    else :
        rate = ((150-calls)* 0.60) + 200
elif 150 < calls <=200 : 
    if not ((200-calls)*0.50) :
        rate = 280.5
    else :
        rate = ((200-calls)*0.50) + 200 + (50*0.60)
elif 200 < calls : rate = (50*0.60 + 50*0.50) + 200 + ((calls - 200)* 0.40)

print(rate)