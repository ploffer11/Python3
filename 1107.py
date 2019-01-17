import itertools 

class RemoteControler:
    def __init__(self):
        self.n = int(input())
        self.m = int(input())
        self.button, self.ans = (
            list(range(10)), abs(self.n-100)
        )

        if self.m != 0:
            for i in map(int,input().split()):
                self.button.remove(i)

    def solve(self):
        l = len(str(self.n))
        self.button = list(map(str, self.button))
        
        if l == 6:
            l -= 1
        
        for i in range(max(1,l-1), l+2):
            for j in itertools.product(self.button, repeat=i):
                self.ans = min(
                    abs(
                        int("".join(j)) - self.n
                    ) + i,
                    self.ans
                )
                
    

remote_controler = RemoteControler()
remote_controler.solve()
print(remote_controler.ans)