from functools import total_ordering
from operator import itemgetter 

@total_ordering
class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string, self.number, self.sort_num = (
            string, number, sort_num 
        )
    
    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string
    
    def __repr__(self):
        return f"{self.string}:{self.number}"
    
def __eq__(self, object):
    return all((
        self.string == object.string,
        self.number == object.number,
        self.sort_num == object.number
    ))

a = WeirdSortee("a", 4, True)
b = WeirdSortee("b", 3, True)
print( a != b )


l = ["hello", "HELP", "Helo"]
l.sort()
print(l)
l.sort(key = str.lower)
print(l)


l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
l.sort(key = itemgetter(1))
print(l)




