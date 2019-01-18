import sys
import random
import string 

class StringJoiner(list):
    def __enter__(self):
        return self


    def __exit__(self, type, value, tb):
        self.result = "".join(self)


with StringJoiner() as joiner:
    for i in range(15):
        joiner.append(random.choice(string.ascii_letters))
    
print (joiner.result)

