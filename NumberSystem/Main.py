import util

def main() :
    Choice  = util.entryCheck("""
Enter 1 for binary to decimal conversion:
Enter 2 for Decimal to binary conversion:
Enter 3 to add two binary numbers       :
Choice: """,
                              r"^[123]{1}$",
                              )
    
    if Choice == 1 :
        number = util.entryCheck("Enter your binary number: ", r"^[01]+$", Type="string")
        print(f"The number in decimal form: {BinaryToDecimal(number)}")
        
    elif Choice == 2:
        binary = util.entryCheck("Enter your decimal number: ", r"^[0-9]+$")
        print(f"The number in binary form is: {DecimalToBinary(binary)}")
    else :
        num1, num2 = util.entryCheck("Enter your two binary numbers (b + b): ", r"^[01]+\s{1}[01]+$",Type="string").strip().split()
        print(f"The total value is: {DecimalToBinary(BinaryToDecimal(num1) + BinaryToDecimal(num2))}")
    
        

def BinaryToDecimal(number: str) :
    AList = []
    for i in number :
        AList.append(i)
    AList = list(map(int, AList))
    
    total = 0
    j = len(AList)-1
    for i in AList :
        total += i * 2**(j)
        j = j-1
    return total

def DecimalToBinary(number: int) :
    remainder = 0
    List = []
    while number != 0 :
        remainder = number%2
        number = number // 2
        List.append(remainder)

    return List[::-1]

    
    
if __name__ == "__main__" :
    main() 
