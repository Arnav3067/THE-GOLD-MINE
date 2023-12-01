import HangMan

def main() :
    
    hangMan = HangMan.Game.initialise()
    print(f'\n*************** Level: {hangMan.level} Name: {hangMan.userName} GUESS THE WORD OR DIE!! ***************\n')
    print('NOTE: if you enter the word directly and get it wrong you will loose instantly')
    while True :
        guess = HangMan.entryCheck(f'\n{hangMan.hiddenWords} Score:{hangMan.score} Lives: {hangMan.lives} wrong letters: {",".join(hangMan.wrongLetters)} Guess a Letter: ', r'^[a-z]+$', Type='string')
        
        if len(guess) >= 3 and guess != hangMan.word :
            
            hangMan.lives -= 7
            if hangMan.lives <= 0:
                print('''

                ______
                ¦  O
                ¦ /¦\ 
                ¦ / \\
                ______          

                ''')
                hangMan.winOrLoose()
                break
        
        if guess == hangMan.word :
            HangMan.printDino()
            print('well done now you are a spelling bee champion')
            restart(input('\nDo you want to play again (y/n)').strip())
        else :
            
            if guess in hangMan.rightLetters :
                print('letter already entered!')
                continue
            
            if guess not in hangMan.word :
                hangMan.printManLimb()
                hangMan.wrongLetters.append(guess)
            else :
                hangMan.checkGuess(guess)
                
            hangMan.hiddenWords = ' '.join(hangMan.listOfHiddenwords)
            
            winOrloose = hangMan.winOrLoose()
            
            if winOrloose == 'won' or winOrloose == 'lost' :
                break
            
    restart(input('\nDo you want to play again (y/n)').strip())
    
    
def restart(r) :
    if r == 'y' :
        main()
    else :
        print('thank you for playing')
        exit()
        
        
            
        
        
        
main()