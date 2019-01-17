from collections import defaultdict
from collections import Counter 

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

