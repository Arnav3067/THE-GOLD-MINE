'''
this program is a suffisticated version of the other one
you can have max 3 input
the key system is universal and not just 3
there is a godd nit of idiot proofing done
the lists at the end are joined into one string aswell.

here are some codes to test this program efficiently(only for key = 3)


1 INPUT
ENCODES

a. bob
b.zack
c.computerrr

DECODES

a.ere
b.shqwdjrqb
c.cdfn

2INPUT
ENCODE

a.arnav kothari
b.united states
c.dominican republic

DECODES

a.duqdy nrwkdul
b.xqlwhg vwdwhv
c.grplqlfdq uhsxeolf

3INPUTS
ENCODE

a.athlone community college
b.sciene is fun
c.god of war

DECODES

a.dwkorqh frppxqlwb froohjh
c.vflhqfh lv ixq
d.jrg ri zdu



'''

print('this progam can handel max three inputs')

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while True :
    num_of_in = int(input('HOW MANY INPUTS DO YOU WANT ? : '))
    if num_of_in == 1 :
        ini_input_1 = []
        final_input_1 = []
        mode = input('SELCT THE MODE : ENCODE    DECODE : ').lower()
        if mode == 'encode' :
            key = int(input('ENTER THE KEY OF THE CYPHERE : '))
            inn = input('ENTER TE MESSAGE TO ENCODE : '  ).lower()
            ini_input_1.extend(inn)
            for i in range(len(ini_input_1)) :
                ini_index = abc.index(ini_input_1[i])
                final_index = ini_index+key
                if final_index > 25 :
                    new_index = final_index-26
                    final_input_1.append(abc[new_index])
                else :
                    final_input_1.append(abc[final_index])
                    
            print(f'THE DECYPHERED CODE IS : {"".join(final_input_1)}')
            
        elif mode == 'decode' :
            key = int(input('ENTER THE KEY OF THE CYPHERE : '))
            inn = input('ENTER TE MESSAGE TO DECODE : '  ).lower()
            ini_input_1.extend(inn)
            for j in range(len(ini_input_1)) :
                ini_index = abc.index(ini_input_1[j])
                final_index = ini_index-key
                if final_index <0 :
                    new_index = 26 + final_index
                    final_input_1.append(abc[new_index])
                else :
                    final_input_1.append(abc[final_index])
                    
            print(f'THE DECIPHERED CODE IS : {"".join(final_input_1)}')
    
    elif num_of_in == 2 :
        ini_input_21 = []
        final_input_21 = []
        ini_input_22 = []
        final_input_22 = []
        mode = input('SELECT A MODE: DECODE    ENCODE : ').lower()
        if mode == 'encode' :
            key = int(input('ENTER THE KEY FOR THE CYPHERE : '))
            inn1,inn2 = input('ENTER YOUR MESSAGE TO ENCODE : ').split()
            inn1.lower()
            inn2.lower()
            ini_input_21.extend(inn1)
            ini_input_22.extend(inn2)
            for k in range(len(ini_input_21)) :
                ini_index_21 = abc.index(ini_input_21[k])
                final_index_21 = ini_index_21+key
                if final_index_21 > 25 :
                    new_index_21 = final_index_21-26
                    final_input_21.append(abc[new_index_21])
                else :
                    final_input_21.append(abc[final_index_21])
                    
            for l in range(len(ini_input_22)) :
                ini_index_22 = abc.index(ini_input_22[l])
                final_index_22 = ini_index_22+key
                if final_index_22 > 25 :
                    new_index_22 = final_index_22-26
                    final_input_22.append(abc[new_index_22])
                else :
                    final_input_22.append(abc[final_index_22])
                    
            print(f'THE DECIPHERED CODE IS : {"".join(final_input_21)} {"".join(final_input_22)}')
            
            
        elif mode == 'decode' :
            key = int(input('ENTER THE KEY FOR THE CYPHERE : '))
            inn1,inn2 = input('ENTER YOUR MESSAGE TO ENCODE : ').split()
            inn1.lower()
            inn2.lower()
            ini_input_21.extend(inn1)
            ini_input_22.extend(inn2)
            for k in range(len(ini_input_21)) :
                ini_index_21 = abc.index(ini_input_21[k])
                final_index_21 = ini_index_21-key
                if final_index_21 < 0  :
                    new_index_21 = 26 + final_index_21
                    final_input_21.append(abc[new_index_21])
                else :
                    final_input_21.append(abc[final_index_21])
                    
            for l in range(len(ini_input_22)) :
                ini_index_22 = abc.index(ini_input_22[l])
                final_index_22 = ini_index_22-key
                if final_index_22 < 0 :
                    new_index_22 = 26+final_index_22
                    final_input_22.append(abc[new_index_22])
                else :
                    final_input_22.append(abc[final_index_22])
                    
            print(f'THE DECIPHERED CODE IS : {"".join(final_input_21)} {"".join(final_input_22)}')
            
    elif num_of_in == 3 :
        ini_input_31 = []
        final_input_31 = []
        ini_input_32 = []
        final_input_32 = []
        ini_input_33 = []
        final_input_33 = []
        mode = input('SELECT A MODE : ENCODE   DECODE : ').lower()
        if mode == 'encode' :
            key = int(input('ENTER THE KEY OF TE CIPHERE : '))
            inn1,inn2,inn3 = input('ENTER YOUR MESSAGE : ').split()
            inn1.lower()
            inn2.lower()
            inn3.lower()
            ini_input_31.extend(inn1)
            ini_input_32.extend(inn2)
            ini_input_33.extend(inn3)
            for m in range(len(ini_input_31)) :
                ini_index_31 = abc.index(ini_input_31[m])
                final_index_31 = ini_index_31 + key
                if final_index_31 > 25 :
                    new_index_31 = final_index_31 - 26
                    final_input_31.append(abc[new_index_31])
                else :
                    final_input_31.append(abc[final_index_31])
                    
            for n in range (len(ini_input_32)) :
                ini_index_32 = abc.index(ini_input_32[n])
                final_index_32 = ini_index_32 + key
                if final_index_32 > 25 :
                    new_index_32 = final_index_32 - 26
                    final_input_32.append(abc[new_index_32])
                else :
                    final_input_32.append(abc[final_index_32])
                    
            for o in range(len(ini_input_33)) :
                ini_index_33 = abc.index(ini_input_33[o])
                final_index_33 = ini_index_33 + key
                if final_index_33 > 25 :
                    new_index_33 = final_index_33 - 26
                    final_input_33.append(abc[new_index_33])
                else :
                    final_input_33.append(abc[final_index_33])
                    
            print(f'THE CYPHERED CODE IS : {"".join(final_input_31)} {"".join(final_input_32)} {"".join(final_input_33)}')
            
        elif mode == 'decode' :
            key = int(input('ENTER THE KEY OF THE CYPHERE'))
            inn1,inn2,inn3= input('ENTER YOUR MESSSAGE : ').split()
            inn1.lower()
            inn2.lower()
            inn3.lower()
            ini_input_31.extend(inn1)
            ini_input_32.extend(inn2)
            ini_input_33.extend(inn3)
            
            for p in range(len(ini_input_31)) :
                ini_index_31 = abc.index(ini_input_31[p])
                final_index_31 = ini_index_31 - key
                if final_index_31 < 0  :
                    new_index_31 = 26 +final_index_31
                    final_input_31.append(abc[new_index_31])
                else :
                    final_input_31.append(ac[final_index_31])
            for q in range(len(ini_input_32)) :
                ini_index_32 = abc.index(ini_input_32[q])
                final_index_32 = ini_index_32 - key
                if final_index_32 < 0  :
                    new_index_32 = 26 + final_index_32
                    final_input_32.append(abc[new_index_32])
                else :
                    final_input_32.append(abc[final_index_32])
                    
            for r in range(len(ini_input_33)) :
                ini_index_33 = abc.index(ini_input_33[r])
                final_index_33 = ini_index_33 - key
                if final_index_33 < 0 :
                    new_index_33 = 26 + final_index_33
                    final_input_33.append(abc[new_index_33])
                else :
                    final_input_33.append(abc[final_index_33])
                    
            print(f'THE DECIPHERED CODE IS : {"".join(final_input_31)} {"".join(final_input_32)} {"".join(final_input_33)}')
            
        else :
            print('MY IDIOT PROOFING WORKED!!!!')
                    
                    
                    
                    
                    
                
                    
                           
                           
                           
                
                           
                           
        
            
            
                    
            
                    
        
    
 
    
    
    


    

    
