import myLibrary

print("THIS PROGRAM RETURNS THE GREATEST OF THREE INTEGERS")

a, b, c = input("enter two numbers: ").split()

print(f"{myLibrary.greatestOfAll2(a,b,c)} is the greatest !!")