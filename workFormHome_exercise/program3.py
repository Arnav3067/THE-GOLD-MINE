import myLibrary

print("THIS PROGRAM RETURNS THE GREATEST OF THREE INTEGERS")

a, b, c = input("enter three integers: ").split()

max = myLibrary.greatestOfAll3(a,b,c)
print(f"{max} is the greatest !!")