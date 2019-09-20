

guesses = []

health = 6

word_solved = False



 


def new_game():
    global health
    while True:
        
        
        
        user_choice = input("Do you want to start a new game? (Y/N)\n")
        try:
            if user_choice == "Y" or user_choice == "y":
                print("Starting a new game...")
                refresh_game()
                hangman()
            elif user_choice == "N" or user_choice == "n":
                break
                exit()
                
        except:
            print("Please type 'y' (yes) or 'n' (no)!")






def refresh_game():
    global health
    global guesses
    global char
    global guess
    global word_solved
    health += 6
    guesses = []
    char = ""
    guess = ""
    word_solved = False





# HANGMAN JATEK
def hangman():
    print()
    global word_solved
    unknown_word = input("What word do you want the other player to guess? \n")
    global health
    count = len(unknown_word) # Variable to trigger win
    global guesses
    
# EZ AKKOR IS NYER, HA UGYAN AZT A BETUT IROD BE 2X AMI AZ UNKNOWN_WORD
    while health > 0:
       
        for char in unknown_word:
            if char in guesses:
                print("  " + char + ",  ", end="")
                
            else:
                
                print("  _,  ", end = "")
            guesses.append(guess)
        print()

        print("Used letters: {}".format(guesses))
        guess = input("Guess a letter: ")
        # increase list with guessed words
        if len(guess) != 1 and guess.isalpha():
            if guess in guesses:
                print("Give me 1 letter only!\nYou already used that letter!")
        

        if guess not in unknown_word:
            guesses.append(guess)
            health -= 1
            if health == 5:
                print(" -----")
                print(" |    |")
                print(" |    0")
                print(" |   ")  
                print("___  ")
                print()
                print(guesses)
            elif health == 4:
                print(" -----")
                print(" |    |")
                print(" |    0")
                print(" |    I")  
                print("___  ")
                print()
                print(guesses)
            elif health == 3:
                print(" -----")
                print(" |    |")
                print(" |    0")
                print(" |   -I")  
                print("___  ")
                print()
                print(guesses)
            elif health == 2:
                print(" -----")
                print(" |    |")
                print(" |    0")
                print(" |   -I-")  
                print("___  ")
                print()
                print(guesses)
            elif health == 1:
                print(" -----")
                print(" |    |")
                print(" |    0")
                print(" |   -I-")  
                print("___  /")
                print()
                print(guesses)
            elif health == 0:
                print(" -----")
                print(" |    |")
                print(" |    0")
                print(" |  --I--")  
                print("___  / \ ")
                print()
                print(guesses)
                print()
                print("You lose!")
                print()
                print("The word was: {}".format(unknown_word))
                new_game() 

    print("You won!")                       
    print("")
    print("The word was {}".format(unknown_word))      
    new_game() 
hangman()

