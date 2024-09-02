import VeryUsefulStuff as vus
import colorama
from colorama import Fore
colorama.init(autoreset=True)

List = vus.entryCheck("Enter the Numbers (With Spaces): ", regex= r"^([0-9]+ *)+$", Type="string").split()
 
print(Fore.RED + "\nRed is for the swaped numbers")
print(Fore.GREEN + "Green is for the unswaped numbers\n")

List = list(map(int, List))
passes = len(List) - 1


def SwapElements(List, pos1, pos2):
    mem = List[pos1] 
    List[pos1] = List[pos2] 
    List[pos2] = mem # and element 2 takes the value of noncurrupted element 1 stored in mem

def ColorPrint(List, rootIndex, color) :
    #List : is the List to be colored
    #rootIndex: is the index of the first number that is being compared
    #color: is the color of the number being printed

    for i in range(len(List)) : # goes through the list and colors the relevant numbers
        if (i == rootIndex or i == rootIndex + 1) :
            print(color + str(List[i]), end=", ")
        else :
            print(List[i], end=", ")
    print()

for passs in range(passes) : # loopoing over the passes

    print(f"\nPass : {passs}")
    swaps = 0
    comparisons = 0
    
    for i in range(len(List) - 1) : # looping through the list of numbers

        a, b= List[i], List[i+1]
        comparisons += 1
        if (a > b) : 
            SwapElements(List, i, i+1) 
       

    print(f"Swaps : {swaps}  Comparisions : {comparisons}")





"""
UserCentered design in the program :

the input system (vus.entryCheck) is very versatile as it uses a regex to check the entry from the console (user),
the output from that function can be recived in many formats such as string, int, list[int], char giving the programmer
a wide variety of choice in the input system

The prompt is laid out in a very simple manner saying 'Enter the numbers (with spaces)' if the user does not enter a string 
that matches the pattern specified in the regex it will simply ask to re-enter the string of numbers.

the final output shows the iteration of every pass and color codes the swaped numbers in red and unswapped numbers in green
to clearly show how the sorting mechanism works
"""
        