class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string, self.number, self.sort_num =(
            string, number, sort_num
        )

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string
    
    def __repr__(self):
        return f"{self.string}:{self.number}"

a = WeirdSortee("a", 4, True)
b = WeirdSortee("b", 3, True)
c = WeirdSortee("c", 2, True)
d = WeirdSortee("d", 1, True)
l = [a,b,c,d]
l.sort()
print( l )