import sys
inname, outname = (
    "_20190118in.txt", "_20190118out.txt"
)

class WarningFilter:
    def __init__(self, insequence):
        self.insequence = insequence
    
    def __iter__(self):
        return self
    
    def __next__(self):
        i = self.insequence.readline()
        while i and "WARNING" not in i:
            i = self.insequence.readline()
        if not i:
            raise StopIteration 
        return i.replace(" WARNING", "")

"""
with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = WarningFilter(infile)
        for i in filter:
            outfile.write(i)
"""

def warnings_filter(insequence):
    for i in insequence:
        if "WARNING" in i:
            yield i.replace(" WARNING", "")

"""
with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = warnings_filter(infile)
        print(filter)
        for i in filter:
            print(i)
        #    outfile.write(i)
"""

def warnings_filter2(infilename):
    with open(infilename) as infile:
        yield from (
            i.replace(" WARNING", "") for i in infile if "WARNING" in i
        )

"""
filter = warnings_filter2(inname)
with open(outname, "w") as outfile:
    for i in filter:
        print(i)
        outfile.write(i)
"""
