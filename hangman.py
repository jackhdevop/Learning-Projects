# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

# secret_word = choose_word(wordlist)
# letters_guessed = []
# warnings = 3
# guesses_left = 6





def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
      if char not in letters_guessed:
          return False
    
    return True
  
   



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word_return = ''
    for letter in secret_word:
      if letter in letters_guessed:
        word_return += letter
      else:
        word_return += '_ '
    

    return word_return

    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''


    letters_left = string.ascii_lowercase
    letters_left_list = list(letters_left)
    outstring = ''
    for letter in letters_guessed:
      if letter in letters_left:
        letters_left_list.remove(letter)
    for char in letters_left_list:
      outstring += char

    return outstring

def analyze(guess):
  '''
    guess: letter that has most recently been guessed. 
    returns: four different possible returns depending on what the guess is.
      1. the guess is not a letter in the alphabet: a warning message letting them 
         know they need to input a letter, and how many warnings are left.
      2. the letter has been guessed already: a warning message saying they have
         already guessed that letter, and how many warnings are left.
      3. the letter is not a correct guess: a message saying that letter is not in 
         the secret word, and get_guessed_word function output
      4. the letter is a correct guess: good guess: get_guessed_word function output
  '''
  all_letters = string.ascii_lowercase
  all_letters_upper = string.ascii_uppercase

  for pos1 in guess:
      x = False
      for pos2 in all_letters:
        if pos1 == pos2:
            x = True
      if x == True:
        break   
      for pos3 in all_letters_upper:
        if pos1 == pos3:
            x = True
      # if warnings > 0:
      #   warnings = warnings - 1
      #   output = "Oops! That is not a valid letter. You have "+ str(warnings) +" warnings left: "
      # else:
      #   guesses_left = guesses_left - 1
      #   output = str("Oops! That is not a valid letter. You have no warnings left so you lose one guess: ")

  # position = 0
  # for char1 in guess:
  #         for char2 in all_letters_upper:
  #           if char1 == char2:
  #             guess = all_letters[position]
  #           position = position + 1


  # for char1 in guess:
  #     x = False
  #     for char2 in letters_guessed:
  #        if char1 == char2:
  #           if warnings > 0:
  #             output = "Oops! You've already guessed that letter. You have "+ str(warnings)+ " warnings left: "
  #             warnings = warnings - 1
  #             x = True
  #           else: 
  #             output = str("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:")
  #             guesses_left = guesses_left - 1
  #             x = True
  #     if x == True:
  #       break
  #     for char1 in guess:
  #       for char2 in secret_word:
  #         if char1 == char2:
  #           output = str("Good guess: ")

  # # newoutput = ''.join(output)

  return x





# letters_guessed = [" "]
# warnings = 3
# guesses_left = 6
# all_letters = string.ascii_lowercase
# all_letters_upper = string.ascii_uppercase
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    import string
    initialstring = string.ascii_lowercase
    initialstringupper = string.ascii_uppercase
    vowel = 'aeiou'
    consonant = 'bcdfghjklmnpqrstvwxyz'
    warnings = 3
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+ str(len(secret_word))+ " letters long.")
    print('You have '+ str(warnings) +' warnings left: ')
    letters_guessed = ''
    num = 6
    get_letter = ''

    while num > 0:
      print("--------------------")
      if is_word_guessed(secret_word, get_letter):
        print ("Congratulations, you won!")
        unique = []
        for char in secret_word[::]:
          if char not in unique:
            unique.append(char)
        
        print("Your total score for this game is: " + str((num*len(unique))))
        break
      print("You have " + str(num) + ' guesses left.')
      print("available letters: " + get_available_letters(letters_guessed))

      char = input('Please guess a letter: ')
      if analyze(char) == False:
        if warnings > 0:
          warnings = warnings - 1
          print("Oops! That is not a valid letter. You have "+ str(warnings) +" warnings left: ")
        else:
          num = num - 1
          print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: ")

      if char in initialstring or initialstringupper:
        loChar = char.lower()
        get_letter += loChar
      outstring = get_guessed_word(secret_word, get_letter)

      if loChar in letters_guessed:
        if loChar not in secret_word:
          if warnings > 0:
            warnings = warnings - 1
            print('Oops! You\'ve already guessed that letter. You have '+ str(warnings) + ' warnings left: ' + outstring)
          else:
            num = num - 1
            print('Oops! You\'ve already guessed that letter. You have '+ str(warnings) + ' warnings left so you lose a guess: ' + outstring)


      if loChar in secret_word:
        if loChar in letters_guessed:

          if warnings > 0:
            warnings = warnings - 1
            print('Oops! You\'ve already guessed that letter. You have '+ str(warnings) + ' warnings left: ' + outstring)
          else:
            num = num - 1
            print('Oops! You\'ve already guessed that letter. You have '+ str(warnings) + ' warnings left so you lose a guess: ' + outstring)
        else:
          print ('Good guess: ' + outstring)
          
        # if loChar in letters_guessed:
        #   if warnings > 0:
        #     warnings = warnings - 1
        #     print('Oops! You\'ve already guessed that letter. You have '+ str(warnings) + ' warnings left: ' + outstring)
          # else:
          #   num = num - 1
          #   print('Oops! You\'ve already guessed that letter. You have '+ str(warnings) + ' warnings left so you lose a guess: ' + outstring)
      elif analyze(char) == False:
        None
      elif loChar not in letters_guessed:
        if loChar in consonant:
          print('Oops! That letter is not in my word: ' + outstring)
          num = num - 1
        else:
          print('Oops! That letter is not in my word: ' + outstring)
          num = num - 2

      if loChar not in letters_guessed:
        letters_guessed += loChar

      if num <= 0:
        print('---------------------')
        print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')

      
      # a = analyze(guess,secret_word,letters_guessed,warnings,guesses_left)
      # print(letters_guessed)
      # letters_guessed.append(guess)
      # print(letters_guessed)
      # print(a + get_guessed_word(secret_word, letters_guessed))
      # print(secret_word)
      # print(letters_guessed)
      # # letters_guessed.append(guess)
      # # letters_guessed = get_guessed_word(secret_word, letters_guessed)
      # letters_guessed_new = get_guessed_word(secret_word, letters_guessed)
      # print("--------------------")
      # if letters_guessed_new != secret_word and warnings == 0:
      #   print("Sorry, you ran out of guesses. The word was " + secret_word)
      #   break
      # if secret_word == letters_guessed:
      #   print("Congratulations, you won!")
      #   print("Your total score for this game is: " + (guesses_left*len(secret_word)))

      




      # print(a)
      # return a 
    






    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = str(my_word)
    my_word_no_space = my_word.replace(' ','')
    comp_word = ''
    count = 0

    if len(my_word_no_space) == len(other_word):
      for char1 in my_word_no_space:
        if char1 == '_':
            comp_word += char1
        elif char1 == other_word[count:count+1]:
            comp_word += char1
        else:
            False
        count += 1
      if comp_word == my_word_no_space:
        return True
    else:
      return False

    # FILL IN YOUR CODE HERE AND DELETE "pass"



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    hint_list = ''

    for word in wordlist:
      if match_with_gaps(my_word, word) == True:
        hint_list += word + ' '
    print(hint_list)
    # FILL IN YOUR CODE HERE AND DELETE "pass"



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    import string
    initialstring = string.ascii_lowercase
    initialstringupper = string.ascii_uppercase
    vowel = 'aeiou'
    consonant = 'bcdfghjklmnpqrstvwxyz'
    warnings = 3
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+ str(len(secret_word))+ " letters long.")
    print('You have '+ str(warnings) +' warnings left: ')
    letters_guessed = ''
    num = 6
    get_letter = ''

    while num > 0:
      print("--------------------")
      if is_word_guessed(secret_word, get_letter):
        print ("Congratulations, you won!")
        unique = []
        for char in secret_word[::]:
          if char not in unique:
            unique.append(char)
        
        print("Your total score for this game is: " + str((num*len(unique))))
        break
      print("You have " + str(num) + ' guesses left.')
      print("available letters: " + get_available_letters(letters_guessed))

      char = input('Please guess a letter: ')
      if analyze(char) == False and char != '*':
        if warnings > 0:
          warnings = warnings - 1
          print("Oops! That is not a valid letter. You have "+ str(warnings) +" warnings left: ")
        else:
          num = num - 1
          print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: ")

      if char in initialstring or initialstringupper:
        loChar = char.lower()
        get_letter += loChar
      outstring = get_guessed_word(secret_word, get_letter)

      if loChar in letters_guessed:
        if loChar not in secret_word:
          if warnings > 0:
            warnings = warnings - 1
            print('Oops! You\'ve already guessed that letter. You have '+ str(warnings) + ' warnings left: ' + outstring)
          else:
            num = num - 1
            print('Oops! You\'ve already guessed that letter. You have '+ str(warnings) + ' warnings left so you lose a guess: ' + outstring)

      if char == '*':
          show_possible_matches(get_guessed_word(secret_word, letters_guessed))

      if loChar in secret_word:
        if loChar in letters_guessed:

          if warnings > 0:
            warnings = warnings - 1
            print('Oops! You\'ve already guessed that letter. You have '+ str(warnings) + ' warnings left: ' + outstring)
          else:
            num = num - 1
            print('Oops! You\'ve already guessed that letter. You have '+ str(warnings) + ' warnings left so you lose a guess: ' + outstring)
        else:
          print ('Good guess: ' + outstring)
          
        # if loChar in letters_guessed:
        #   if warnings > 0:
        #     warnings = warnings - 1
        #     print('Oops! You\'ve already guessed that letter. You have '+ str(warnings) + ' warnings left: ' + outstring)
          # else:
          #   num = num - 1
          #   print('Oops! You\'ve already guessed that letter. You have '+ str(warnings) + ' warnings left so you lose a guess: ' + outstring)
      elif analyze(char) == False:
        None
      elif loChar not in letters_guessed:
        if loChar in consonant:
          print('Oops! That letter is not in my word: ' + outstring)
          num = num - 1
        else:
          print('Oops! That letter is not in my word: ' + outstring)
          num = num - 2

      if loChar not in letters_guessed:
        letters_guessed += loChar

      if num <= 0:
        print('---------------------')
        print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')

        
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

dog = "apple"
if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
    # hangman(dog)

# secret_word = choose_word(wordlist)
# hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(dog)
