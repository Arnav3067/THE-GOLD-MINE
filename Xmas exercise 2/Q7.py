import utility

weight = utility.entryCheck("Enter your weight: ", r"^\d*\.?\d{1,3}$", Type="float")
height = utility.entryCheck("Enter your height: ", r"^\d*\.?\d{1,3}$", Type="float")

BMI = weight/(height ** 2) 

if BMI < 18.5 :
    print("you weigh so light that you can move faster than lightSpeed")
elif 18.5 <= BMI < 25 :
    print("You are Normal! but are you? ")
elif 25 <= BMI < 30 :
    print("overWeight")
else :
    print('"I have OCD".....\nNaah dude you have OBCD')
