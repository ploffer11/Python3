import sys 
import queue
from collections import namedtuple 

Log = namedtuple("Log", "r c state")

class MoveLog:
    def __init__(self):
        self.n = int(input())
        self.graph = [
            list(input()) for i in range(self.n)
        ]
        self.visit = [
            [ {} for i in range(self.n) ] for j in range(self.n)
        ]
        for i in range(self.n):
            for j in range(self.n):
                b, e = (
                    self.check_pos("B", i, j), self.check_pos("E", i, j)
                )
                if b:
                    self.start = Log(i, j, b)
                elif e:
                    self.end = Log(i, j, e)

        self.act = [
            self.up, self.down, self.left, self.right, self.trans
        ]

    def check(self, *args):
        for i in args:
            if not 0 <= i < self.n:
                return False
        return True 
    
    def check_this(self, this, *args):
        for i in args:
            if not this == i:
                return False
        return True

    def check_pos(self, this, i, j):
        cond1 = (
            self.check(i-1, i+1) and 
            self.check_this(
                this, self.graph[i-1][j], self.graph[i+1][j]
            ) 
        )
        cond2 = (
            self.check(j-1, j+1) and
            self.check_this(
                this, self.graph[i][j-1], self.graph[i][j+1]
            )
        )
        if cond1:
            self.graph[i-1][j], self.graph[i][j], self.graph[i+1][j] =(
                "0", "0", "0"
            )
            return "UD"
        elif cond2:
            self.graph[i][j-1], self.graph[i][j], self.graph[i][j+1] =(
                "0", "0", "0"
            )
            return "LR"
        else:
            return False 

    def up(self, i, j, state):
        if state == "LR":
            if self.check(i-1, j-1, j+1) and self.check_this(
                "0", 
                self.graph[i-1][j-1],
                self.graph[i-1][j],
                self.graph[i-1][j+1]
            ):
                return Log(i-1, j, state)
        else:
            if self.check(i-2) and self.check_this(
                "0",
                self.graph[i-2][j]
            ):
                return Log(i-1, j, state)
        return False
    
    def down(self, i, j, state):
        if state == "LR":
            if self.check(i+1, j-1, j+1) and self.check_this(
                "0", 
                self.graph[i+1][j],
                self.graph[i+1][j-1],
                self.graph[i+1][j+1]
            ):
                return Log(i+1, j, state)
        else:
            if self.check(i+2) and self.check_this(
                "0",
                self.graph[i+2][j]
            ):
                return Log(i+1, j, state)
        return False

    def left(self, i, j, state):
        if state == "UD":
            if self.check(i-1, i+1, j-1) and self.check_this(
                "0", 
                self.graph[i-1][j-1],
                self.graph[i][j-1],
                self.graph[i+1][j-1]
            ):
                return Log(i, j-1, state)
        else:
            if self.check(j-2) and self.check_this(
                "0",
                self.graph[i][j-2]
            ):
                return Log(i, j-1, state)
        return False

    def right(self, i, j, state):
        if state == "UD":
            if self.check(i-1, i+1, j+1) and self.check_this(
                "0", 
                self.graph[i-1][j+1],
                self.graph[i][j+1],
                self.graph[i+1][j+1]
            ):
                return Log(i, j+1, state)
        else:
            if self.check(j+2) and self.check_this(
                "0",
                self.graph[i][j+2]
            ):
                return Log(i, j+1, state)
        return False
    
    def trans(self, i, j, state):
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if not self.check(i+di, j+dj) \
                or self.graph[i+di][j+dj] != "0":
                    return False
        if state == "LR": 
            return Log(i, j, "UD")
        else:
            return Log(i, j, "LR") 
    
    def ans(self, log):
        return (
            log.r == self.end.r and
            log.c == self.end.c and
            log.state == self.end.state
        )

    def solve(self):
        ans = False 
        q = queue.Queue(-1)
        q.put(
            (0, self.start)
        )
        while not q.empty() and not ans:
            time, log = q.get()
            #print(time, log)
            for func in self.act:
                k = func(log.r, log.c, log.state)
                if k and self.visit[k.r][k.c].get(
                    k.state, True 
                ):
                    self.visit[k.r][k.c][k.state] = False
                    q.put((time+1, k))
                    if self.ans(k):
                        ans = (True, time+1)
        if ans:
            print(ans[1])
        else:
            print(0)

main = MoveLog()
main.solve() 