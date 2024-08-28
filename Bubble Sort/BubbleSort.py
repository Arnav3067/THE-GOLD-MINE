List = input("\nEnter thy numbers (With spaces) : ").split()
print()
List = list(map(int, List))

passes = len(List) - 1

for passs in range(passes) : # loopoing over the passes

    print(f"\nPass : {passs}")
    swaps = 0
    
    for i in range(len(List) - 1) : # looping through the list
        print(List)
        a = List[i]
        b = List[i+1]
        
        if (a > b) :
            List.pop(i)
            List.pop(i) # this function works on the list after the first pop hence now it has on less element 
            # than before the first pop, hence to pop the adjacent element (which is now the first element) 
            # you just use i
            List.insert(i, b)
            List.insert(i+1, a)
            swaps += 1

    print(f"Swaps : {swaps}")

    
        