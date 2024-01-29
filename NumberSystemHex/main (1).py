import util

HexaLetters = {
  "A": 10,
  "B": 11,
  "C": 12,
  "D": 13,
  "E": 14,
  "F": 15,
}

HexaNumbers = {
  10: "A",
  11: "B",
  12: "C",
  13: "D",
  14: "E",
  15: "F"
}


def main():
  Choice = util.entryCheck("""
Enter 1 for Decimal to HexaDecimal
Enter 2 for HexaDeccimal to Decimal
Enter 3 for Binary to HexaDecimal
Engter 4 for HexaDecimal to Binary
Choice: """,
r"^[1-4]{1}$")

  if Choice == 1 :
    number = util.entryCheck("Enter the Number: ", r"^[0-9]+$")
    print(f"the HexaDecimal form of {number} is: {DecimalToHexa(number)}")
  elif Choice == 2 :
    number = util.entryCheck("Enter the number: ", r"^[0-9A-F]+$", Type="string")
    print(f"the decimal form of {number} is: {HexaToDecimal(number)}")
  elif Choice == 3 :
    number = util.entryCheck("Enter the number: ", r"^[0-1]+$", Type="string")
    print(f"the Hexadecimal form of {number} is: {BinaryToHexa(number)}")
  else :
    number = util.entryCheck("Ener the number: ", r"^[0-9A-F]+$", Type="string")
    print(f"the Binary form of {number} is: {HexaToBinary(number)}")

def HexaToDecimal(number) -> int:
  j = 0
  total = 0
  
  for i in number[::-1]:
    if i.isalpha():
      total += HexaLetters[i] * 16**j
    else:
      total += int(i) * 16**j
    j += 1
  return total


def DecimalToHexa(number) -> str:
  remainder = 0
  total = ""
  
  while number != 0 :
    remainder = number % 16
    number = number // 16
    if remainder > 9 :
      total += HexaNumbers[remainder]
    else :
      total += str(remainder)
      
  return total[::-1]
  
def HexaToBinary(number) :
  BinaryList = []
  
  for i in number :
    if i.isalpha() :
      BinaryList.append(util.FillTheGap(util.DecimalToBinary(HexaLetters[i]), 4))
    else :
      BinaryList.append(util.FillTheGap(util.DecimalToBinary(int(i)), 4))

  return ''.join(BinaryList)

def BinaryToHexa(number) :
  List = []
  count = 0
  total = ""
  Number = number
  for i in number :
    total += i
    count += 1
    if count > 3 :
      List.append(total)
      Number = Number.replace(total, "")
      count = 0
      total = ""
      
  if len(number) % 4 != 0:
    List.append(util.FillTheGap(Number, 4))

  List = list(map(util.BinaryToDecimal, List))
  for index, element in enumerate(List) :
    if element > 9 :
      List[index] = HexaNumbers[element]

  List = list(map(str, List))
  return "".join(List)

if __name__ == "__main__":
  main()
