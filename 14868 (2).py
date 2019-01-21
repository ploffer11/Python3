import queue 
import sys
from collections import namedtuple

sys.setrecursionlimit(200000)
read = lambda : map(int, sys.stdin.readline().split())
Pos = namedtuple("Pos", "r c num")


n, k = read()
graph = [
    [0] * n for i in range(n)
]
visit = [
    [False] * n for i in range(n)
]
parent = [0] * 100005
pos = []
for i in range(1,  k+1):
    r, c = read()
    r, c = r-1, c-1
    graph[r][c] = i
    pos.append(
        Pos(r, c, i)
    )

def find(me):
    if  parent[me] == 0:
        return me
    else:
        parent[me] =  find( parent[me])
        return  parent[me]

def union(a, b):
    if a == 0 or b == 0:
        return 
    a, b =  find(a),  find(b)
    if a != b:
         parent[a] = b 

def union_near(r, c):
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        if  check_board(r+dr, c+dc):
             union(
                 graph[r][c],  graph[r+dr][c+dc]
            )
    
def check():
    while  pos:
        if  find( pos[-1].num) ==  find(1):
             pos.pop()
        else:
            return False
    return True 

def check_board(*args):
    for i in args:
        if not 0<=i<n:
            return False
    return True    

def bfs_near(r, c, num):
    args = []
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        if  check_board(r+dr, c+dc) and not  visit[r+dr][c+dc]:
            visit[r+dr][c+dc] = True
            args.append(Pos(r+dr, c+dc, num))
    return args

def debug():
    for i in  graph:
        for j in i:
            print( find(j), end = " ")
        print()
    print()

def solve():
    q = queue.Queue(-1)
    for i in  pos:
        q.put(i)
        visit[i.r][i.c] = True
    ans = -1
    #debug() 
    while not q.empty() and not  check():
        ans += 1
        for j in range(q.qsize()):
            r, c, num = q.get()
            union_near(r, c)
            for i in  bfs_near(r, c, num):
                q.put(i)
        #debug()
        #print(q.qsize(), end = " ")
        for j in range(q.qsize()):
            r, c, num = q.get()
            q.put(Pos(r, c, num))
            graph[r][c] = num
    print(ans) 

solve()