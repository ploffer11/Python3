normal_list = [1,2,3,4,5]

class CustomSequence:
    def __len__(self):
        return 5

    def __getitem__(self, index):
        return f"x{index}"

class FunkyBackwards:
    def __reversed__(self):
        return "BACKWARDS"


for seq in normal_list, CustomSequence(), FunkyBackwards():
    print(f"\n{seq.__class__.__name__}: ", end="")
    for item in reversed(seq):
        print(item, end=", ")
    

class yusalist:
    def __len__(self):
        return 3

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError("murry byungsin")
            #raise BaseException("murry byungsin")
        return "x%d"%(index)

for i in reversed(yusalist()):
    print(i, end=", ")

print ("\n ***************************")

for i in yusalist():
    print(i, end=", ")    