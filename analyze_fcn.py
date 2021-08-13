import string
guess = "x"

letters_guessed = ["a", "b", "c", "d" , "l", "e"]
secret_word = ['a', 'l', 'e', 'x']
warnings = 0
guesses_left = 6


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word_return = ["_ "]

    for i in range( len( secret_word ) - 1 ):
      word_return.append("_ ")
    position = 0
    for char1 in secret_word:
      for char2 in letters_guessed:
        if char1 == char2:
          word_return[position] = char1
      position = position + 1
    word_return = ''.join(word_return)
    return word_return


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
    if x == True:
        break
    if warnings > 0:
                    output = "Oops! That is not a valid letter. You have "+ str(warnings) +" warnings left: "
                    warnings = warnings - 1
    else:
                    output = str("Oops! That is not a valid letter. You have no warnings left so you lose one guess: ")
                    guesses_left = guesses_left - 1

position = 0
for char1 in guess:
      for char2 in all_letters_upper:
        if char1 == char2:
          guess = all_letters[position]
        position = position + 1


for char1 in guess:
      x = False
      for char2 in letters_guessed:
        if char1 == char2:
          if warnings > 0:
            output = str("Oops! You've already guessed that letter. You have "+ str(warnings)+ " warnings left: ")
            warnings = warnings - 1
            x = True
          else: 
            output = str("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:")
            guesses_left = guesses_left - 1
            x = True
      if x == True:
            break
      for char1 in guess:
       for char2 in secret_word:
         if char1 == char2:
           letters_guessed.append(guess)
           output = str("Good guess: ")

word_return = get_guessed_word(secret_word, letters_guessed)
print(word_return)
print(secret_word)

secret_word = ''.join(secret_word)
print(word_return)
print(secret_word)

# output = ''.join(output)

while secret_word != word_return:
  print("NO")
  break

print( output , get_guessed_word(secret_word, letters_guessed))

print(letters_guessed)

# print(output)
    

