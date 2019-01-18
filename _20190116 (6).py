from collections import defaultdict
from collections import Counter 
import string

def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    
def letter_frequency2(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

def letter_frequency3(sentence):
    return Counter(sentence)

CHARACTERS = list(string.ascii_letters) + [" "]

def letter_frequency4(sentence):
    frequencies = [ (c, 0) for c in CHARACTERS ]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1] + 1)
    return frequencies


responses = [ 
    "vanilla",
    "chocolate",
    "vanilla",
    "vanilla",
    "caramel",
    "strawberry",
    "vanilla" 
]

print(
    "The children voted for {} ice cream".format(
        Counter(responses).most_common(1)    
        )
)


