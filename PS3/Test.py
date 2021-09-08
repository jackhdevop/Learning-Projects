SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

word = 'Fork'
n = 4

word = word.lower()
# print(word)
var = 0
for let in word:
    var += SCRABBLE_LETTER_VALUES[let]
# print (var)
var2 = (7 * len(word)) - (3 * (n - len(word)))
# print (var2)
if var2 < 0:
    var2 = 1


result = var * var2
print(result)