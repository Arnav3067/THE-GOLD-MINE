import math

sides = list(map(int, input("Enter the sides of the triangle: (separated via a space): ").split()))
s = sum(sides)/2
area = math.sqrt(s*(s-sides[0])*(s-sides[2])*(s-sides[1]))

print("Area: ", area)


