"""
Baekjoon online judge
problem num : 3830

WHY RTE??????????????????????? 
"""

import sys 
read = lambda : sys.stdin.readline().split()
write = sys.stdout.write

def find(me):
    global parent 
    if parent[me][0] == 0:
        return [me, 0] 

    else:
        pnum, weight = find( parent[me][0] )
        parent[me] = [ pnum, weight + parent[me][1] ]    
        return parent[me]


def union(a, b, c):
    global parent 
    pa, pb = find(a), find(b)
    if pa[0] != pb[0]:
        parent[ pa[0] ] = [ pb[0],  (pb[1] - pa[1]) + c ]
        


while 1:
    N, M = map(int, read()) 

    if N+M==0:
        break 
    
    parent = [ [0, 0] for i in range(N+5) ] 
    
    for _ in range(M):
        R = read()

        if len(R) == 4:
            A, B, C = int(R[1]), int(R[2]), int(R[3])
            union(A, B, C)
        
        else:   
            A, B = find(int(R[1])), find(int(R[2]))
            # print (A, B)
            if A[0] != B[0]:
                write("UNKNOWN\n")
            else:
                write("%d\n"%(A[1] - B[1]))