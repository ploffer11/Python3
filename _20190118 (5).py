class CapitalIterable:
    def __init__(self, string):
        self.string = string
    
    def __iter__(self):
        return CapitalIterator(self.string)

class CapitalIterator:
    def __init__(self, string):
        self.words, self.index = (
            [w.capitalize() for w in string.split()], 0
        )

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        
        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self

iterable = CapitalIterable(
    "the quick brown fox jumps over the lazy dog"
)
iterator = iter(iterable)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


# not iterator
for x in iterable:
    print(x)

