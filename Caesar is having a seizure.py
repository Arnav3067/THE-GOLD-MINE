abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
initial = []
final = []

print('this prorame only handels one input')

while True :
    
    u1 = input('SELECT MODE : DECODE     ENCODE : ').lower()
    if u1 == 'encode' :
        key = int(input('ENTER THE KEY OF THE CYPHERE'))
        inn = input('ENTER YOUR MESSAGE TO ENCODE : ').lower()
        initial.extend(inn)
        for i in range(len(initial)) :
            ini_index = abc.index(initial[i])
            final_index = ini_index+key
            final.append(abc[final_index])
            
        print(f'THE CYPHERED CODE IS : {"".join(final)}')
        
    elif u1 == 'decode' :
        key = int(input('ENTER THE KEY OF THE CYPHERE'))
        inn = input('ENTER YOUR MESSAGE TO DECODE : ').lower()
        initial.extend(inn)
        for i in range(len(initial)) :
            ini_index = abc.index(initial[i])
            final_index = ini_index-key
            final.append(abc[final_index])
            
        print(f'THE DECYPHERED CODE IS : {"".join(final)}')
        
    else :
        print('MY IDIOT PROOFING WORKED!!!!')
        
    
    
    


    

    
