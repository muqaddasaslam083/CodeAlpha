import random


word_list = ["ant", "cat", "zebra", "orange", "grape", "melon", "kiwi", "peach"]

def get_word():
    
    return random.choice(word_list).upper()

def display_word(word, guessed_letters):
   
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def display_hangman(tries):
    
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[6 - tries]

def hangman():
   
    word = get_word()
    guessed_letters = []
    tries = 6
    
    print("Welcome to Hangman!")
    
    while tries > 0:
        
        print(display_hangman(tries))
        
       
        print(display_word(word, guessed_letters))
        
        
        guess = input("Guess a letter: ").upper()
        
       
        if len(guess) == 1 and guess.isalpha():
            
            if guess in guessed_letters:
                print("You already guessed that letter!")
            
            elif guess in word:
                print("Good guess!")
                guessed_letters.append(guess)
               
                if all(letter in guessed_letters for letter in word):
                    print("Congratulations! You guessed the word:", word)
                    break
            else:
                print("Sorry, that letter is not in the word.")
                tries -= 1
        else:
            print("Please enter a single letter.")
        
      
        print("Tries left:", tries)
    
   
    if tries == 0:
        print("Sorry, you ran out of tries. The word was:", word)


hangman()
