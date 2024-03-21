import VeryUsefulStuff as vus

class Convert : 
    
    def BinaryToDecimal(self, number: str) :
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

    
    def ConvertPhraseToBinary(self, string) :
        value = ''
        List = []
        for i in string :
            value += str(ord(i))
            List.append(value)
            value = ''
            
        return list(map(self.DecimalToBinary, List))      


    def ToUnicode(self, List: list[str]) :
        
        for i in range(len(List)):
            if len(List[i]) <= 7 :
                List[i] = self.Byte1(List[i])
            elif 7 < len(List[i]) <= 11 :
                List[i] = self.Byte2(List[i])
            elif 11 < len(List[i]) <= 16 :
                List[i] = self.Byte3(List[i])
            elif 16 < len(List[i]) <= 21 :
                print("byte 4")

        return List
        

    def Byte1(self, string) :
        buffer = 7 - len(string)
        fixedDigits = "0" + ("0" * buffer)
        
        return fixedDigits + string
    
    def Byte2(self, string) :
        buffer = 11 - len(string)
        unicode = ''
        counter = 0
        fixedDigits = "110" + ("0" * buffer)
        
        for i in string[::-1]:
            unicode += i
            counter += 1
            
            if (counter == 6) :
                unicode += "01"
            
        unicode += fixedDigits[::-1]
        
        return unicode[::-1]


    def Byte3(self, string) :
        buffer = 16 - len(string)
        fixedDigits = "1110" + ("0" * buffer)
        unicode = ''
        counter = 0
        
        for i in string[::-1]:
            unicode += i
            counter += 1
            
            if (counter == 6) :
                unicode += "01"
                
            if (counter == 12) :
                unicode += "01"
                
                
        unicode += fixedDigits[::-1]
        
    
        return unicode[::-1]

    
    

    
    
    def Byte4(self, string) :
        buffer = 16 - len(string)
        fixedDigits = "11110" + ("0" * buffer)
        unicode = ''
        counter = 0
        
        for i in string[::-1]:
            unicode += i
            counter += 1
            
            if (counter == 6) :
                unicode += "01"
                
            if (counter == 12) :
                unicode += "01"
                
            if (counter == 18) :
                unicode += "01"
                
        unicode += fixedDigits[::-1]
        
    
        return unicode[::-1]
    
    
    
    
    
    
    
    def DecimalToBinary(self, number) :
        remainder = 0
        List = []
        number = int(number)
        while number != 0 :
            remainder = number%2
            number = number // 2
            List.append(str(remainder))

        return ''.join(List[::-1])
    
    
    
    ''.encode()

def main() :
    
    convert = Convert()
    
    print(ord("𒀀"))
        
    print(convert.ToUnicode(convert.ConvertPhraseToBinary("𒀀")))

if __name__ == "__main__" :
    main()