import sys
read = lambda : int(sys.stdin.readline())
write = sys.stdout.write 

class Stack:
    def __init__(self):
        self.n = read()
        self.stack, self.ans, self.sequence = (
            [], [], []
        )
        for _ in range(self.n):
            self.sequence.append(read())

    def solve(self):

        i, j= 0, 0
        while i<self.n and j<=self.n:
            if self.stack and self.stack[-1] == self.sequence[i]:
                self.ans.append("-")
                self.stack.pop()
                i += 1
            else:
                self.stack.append(j+1)
                self.ans.append("+")
                j += 1
        
        if j > self.n:
            print("NO")
        else:
            print("\n".join(self.ans))

s = Stack()
s.solve() 