import math

def AddPrefixTo(word, pre) :
    return pre + word

def AddPostfixTo(word, post) :
    return word + post

def GetAreaOfCircle(r) :
    return math.pi * r * r

def GetPerimeterOfCircle(r) :
    return 2 * math.pi * r

def GetPerimeterOfRect(a, b) :
    return 2*a + 2*b

def GetAreaOfRect(a, b) :
    return a * b

def main() :
    PrintMenu()
    choice = input("Enter your choice :")
    
    match int(choice) :
        case 1 :
            r = input("Enter the radius: ")
            print(f"the area of the circle with radius {r} is  : {GetAreaOfCircle(int(r))}")
        case 2 :
            r = input("Enter the radius: ")
            print(f"the perimeter of the circle with radius {r} is  : {GetPerimeterOfCircle(int(r))}")
        case 3 :
            a, b = input("Enter the sides of the rect : ").split()
            print(f"The area of the rect is : {GetAreaOfRect(int(a), int(b))}")
        case 4 :
            a, b = input("Enter the sides of the rect : ").split()
            print(f"The perimeter of the rect is : {GetPerimeterOfRect(int(a), int(b))}")
    
def PrintMenu() :
    print("""
1. Area of circle
2. Perimeter of circle
3. Area of rect
4. Perimeter of rect
""")
    
main()