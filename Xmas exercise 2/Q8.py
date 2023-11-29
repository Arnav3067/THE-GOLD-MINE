import utility


def checkStuff(avg) :
    if 0 <= avg < 60 :return("F")
    elif 60 <= avg < 70 :return("D")
    elif 70 <= avg < 80 :return("C")
    elif 80 <= avg < 90 :return("B")
    else :return("A")


sub1 = utility.entryCheck("Enter marks in subject1: ", r"^[0-9]{1,3}$")
sub2 = utility.entryCheck("Enter marks in subject2: ", r"^[0-9]{1,3}$")
sub3 = utility.entryCheck("Enter marks in subject3: ", r"^[0-9]{1,3}$")

if 100 >= max([sub1,sub2,sub3]) :
    avg = sum([sub1, sub2, sub3])/3
    print(checkStuff(avg))
else:
    print("you are bad at lying")



