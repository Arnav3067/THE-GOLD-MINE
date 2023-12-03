import random
import re
class Game :
    
    def __init__(self, userName, words, level) :
        
        self.level = level
        self.userName = userName
        self.word = random.choice(words)
        self.hiddenWords = "_ " * len(self.word)
        self.listOfHiddenwords = self.hiddenWords.split()
        self.lives = 7
        self.manCounter = 0
        self.score = 0
        self.wrongLetters = []
        self.rightLetters = []
        self.Man = {
                0 : "-----------",
                1 : " |     O\n",
                2 : "|   /",
                3 : "|",
                4 : "\\\n",
                5 : "|     |\n",
                6 : "|   / ",
                7 : "\\",
            }
        
    @classmethod
    def initialise(cls) :
        
        userName = input("Enter the username: ").strip()
        level = int(input('Enter level (1-3): '))
        
        if level == 1 : return cls(userName, ['hello', 'world', 'code'], level)
        elif level == 2 : return cls(userName, ['whales', 'resistance', 'computers', 'hemoglobin', 'velocity'], level)
        elif level == 3 : return cls(userName, ['python', 'friction', 'javascript', 'css', 'hitler'], level)
        
        


    def printManLimb(self) :
        self.lives -= 1
        self.manCounter += 1
        
        print('\n\n')
        print(self.Man[0])
        for i in range(1, self.manCounter + 1) :
            print(self.Man[i], end= ' ')
        print('\n')
        
    def checkGuess(self, guess) :
        for i, letter in enumerate(self.word) :
            if letter == guess :
                self.listOfHiddenwords[i] = guess
                self.rightLetters.append(guess)
                self.score += 1
    
    def winOrLoose(self) :
        if self.score == len(self.word) :
            print(f'\n{self.word} was the word !! you won !! ')
            return 'won'
        if self.lives == 0 :
            print(f'\n{self.word} was the word !! you lost !! ')
            return 'lost'




def entryCheck(inputMessage : str, regex : str, errorMessage="" ,Type="int"):
    while True:
        Input = input(inputMessage).strip()
        if re.search(regex, Input) :
            if Type == "float" : return float(Input)
            if Type == "int" :return int(Input)
            if Type == "string" or Type == "char" : return Input
        else :
            if not errorMessage :
                pass
            else:
                print(errorMessage, end='......')
                
                
def printDino():
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠀⠀⠀⢀⣼⠙⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣸⠻⢏⡉⠀⠛⠒⠋⠙⢲⡔⢛⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⠞⠙⣆⣠⠟⠀⠀⠀⠀⠀⠈⠳⠾⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣄⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣅⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡼⢲⣿⠷⠀⠀⠀⠿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰⠃⠀⠀⢰⡤⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠷⢲⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢧⡀⠀⠀⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠲⣞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡤⠽⠶⠤⠧⠼⠦⠤⠤⠴⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣿⣖⠚⠚⠛⠓⠒⠒⠒⠒⣾⠞⠁⠀⠀⠀⠀⠀⠀⠀⠰⡞⠋⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢿⠈⠙⢲⡄⠀⠀⢀⡤⠖⠋⠁⠀⠀⣤⣤⡾⠃⠀⠀⠀⠀⠙⠻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠓⢶⠚⠁⠀⠀⠸⢤⣀⣀⣠⣤⡜⢷⣼⠀⠀⠀⠀⠀⠀⠀⠀⠈⣦⠞⡇⠀⠀⠀⠀⠀⠀
⣴⣄⣀⣿⠀⣀⠀⠀⣴⡄⠀⣸⡧⠞⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠾⠓⠦⣼⣹⡶⢚⠀
⣿⠞⠋⢹⡄⣿⣿⢾⣽⡷⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣠⠟⠀
⢸⡄⠀⠘⣿⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⢄⣠⠞⠁⠀⠀
⠀⢷⣤⣀⣿⣿⡿⢷⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣖⣀⡀⠀⣒⣒⣫⠤⠴⠚⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣦⣀⣠⡤⠤⠴⠒⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
