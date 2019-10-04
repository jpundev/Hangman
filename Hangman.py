from random_word import RandomWords
import os

def main():
    #Generate initial login screen
    print("Welcome to Hangman")
    input("Press any button to begin")
    cls()



    #Variables and random word declaration

    r_word = RandomWords()
    word = r_word.get_random_word()
    lives = 5


    #make word into a list to iterate
    word_list = list(word)
    templist = []
    word_len = len(word_list)
    choices = []
    choicelist = []
    
    for x in word_list:
        templist.append("_")

    
    while True:
        counter = 0
        print("Lives remaining: " + str(lives))
        print("Letters Used: " + ' '.join(choicelist))
        choice = input("Pick a letter: ")
        choicelist.append(choice)
        for index,letter in enumerate(word_list):
            
            if(choice == letter) and (templist[index] != "_"):
                pass
                
            elif(choice == letter) and (templist[index] == "_"):
                
                templist[index] = choice
                counter +=1 
                
             
            
            
        print(' '.join(templist))
        
        if counter == 0:
            lives -= 1
        
        if lives==0:
            print("You lose! ")
            print("The word was " + word)
            break
        
        if "_" not in templist:
            print("You win!")
            break

            




    
                




    


    


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


    

























if __name__ == "__main__":
    main()
    pass