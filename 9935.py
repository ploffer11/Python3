class Explosion:
    def __init__(self):
        self.string, self.bomb, self.stack = (
            input(), input(), []
        )
        self.n, self.m = (
            len(self.string), len(self.bomb)
        )

    def solve(self):
        i, j = 0, 0
        while i < self.l:
            if self.string[i] == self.bomb[j]:
                i = self.stack.append(i)
            i += 1

    def bomb_it(self, i, j):
        while 





        
