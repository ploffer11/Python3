import queue 
import sys
from collections import namedtuple
from collections import deque

sys.setrecursionlimit(200000)
read = lambda : map(int, sys.stdin.readline().split())
Pos = namedtuple("Pos", "r c num")

class Civilization:
    def __init__(self):
        self.n, self.k = read()
        self.graph = [
            [0] * self.n for i in range(self.n)
        ]
        self.visit = [
            [False] * self.n for i in range(self.n)
        ]
        self.parent = [0] * 100005
        self.pos = []
        for i in range(1, self.k+1):
            r, c = read()
            r, c = r-1, c-1
            self.graph[r][c] = i
            self.pos.append(
                Pos(r, c, i)
            )
     
    def find(self, me):
        if self.parent[me] == 0:
            return me
        else:
            self.parent[me] = self.find(self.parent[me])
            return self.parent[me]

    def union(self, a, b):
        if a == 0 or b == 0:
            return 
        a, b = self.find(a), self.find(b)
        if a != b:
            self.parent[a] = b 
    
    def union_near(self, r, c):
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            if self.check_board(r+dr, c+dc):
                self.union(
                    self.graph[r][c], self.graph[r+dr][c+dc]
                )
        
    def check(self):
        while self.pos:
            if self.find(self.pos[-1].num) == self.find(1):
                self.pos.pop()
            else:
                return False
        return True 

    def check_board(self, *args):
        for i in args:
            if not 0<=i<self.n:
                return False
        return True    

    def bfs_near(self, r, c, num):
        args = []
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            if self.check_board(r+dr, c+dc) and not self.visit[r+dr][c+dc]:
                self.visit[r+dr][c+dc] = True
                args.append(Pos(r+dr, c+dc, num))
        return args

    def debug(self):
        for i in self.graph:
            for j in i:
                print(self.find(j), end = " ")
            print()
        print()

    def solve(self):
        q = deque()
        for i in self.pos:
            q.append(i)
            self.visit[i.r][i.c] = True
        ans = -1
        #self.debug() 
        while not self.check():
            ans += 1
            for j in range(len(q)):
                r, c, num = q.popleft()
                self.union_near(r, c)
                for i in self.bfs_near(r, c, num):
                    q.append(i)
            #self.debug()
            #print(q.qsize(), end = " ")
            for j in range(len(q)):
                r, c, num = q.popleft()
                q.append(Pos(r, c, num))
                self.graph[r][c] = num
        print(ans) 

obj = Civilization()
obj.solve()