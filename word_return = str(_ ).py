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


my_word = '__ee'
wordlist = ['free', 'dollar', 'gree']
hint_list = ''

for word in wordlist:
      if match_with_gaps(my_word, word) == True:
        hint_list += word + ' '
print(hint_list)