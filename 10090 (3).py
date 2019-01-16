import math
import sys
import bisect

def Merge(List1, List2):
    Merged = []
    Index1, Index2 = 0, 0
    while 1:
        if Index1==len(List1):
            Merged += List2[Index2:]
            break
        elif Index2==len(List2):
            Merged += List1[Index1:]
            break

        if List1[Index1] < List2[Index2]:
            Merged += [ List1[Index1] ]
            Index1 += 1
        else:
            Merged += [ List2[Index2] ]
            Index2 += 1
        
    return Merged
    
def Init(Node, Start, End):
    global Tree, Arr 

    if Start == End:
        Here = Start #Here = Start = End
        Tree[Node] = [ Arr[Here] ]
        return Tree[Node]

    Mid = (Start + End) // 2
    LeftChild = Init(2*Node, Start, Mid)
    RightChild = Init(2*Node + 1, Mid+1, End)
    Tree[Node] = Merge(LeftChild, RightChild)

    return Tree[Node]

def Solve(Node, Start, End, Left, Right):
    global Tree, K

    if Right<Start or End<Left:
        return 0

    if Left <= Start and End <= Right:
        # print (Tree[Node])
        return bisect.bisect_left(Tree[Node], K)

    Mid = (Start + End) // 2
    LeftChild = Solve(2*Node, Start, Mid, Left, Right)
    RightChild = Solve(2*Node + 1, Mid+1, End, Left, Right)

    return LeftChild + RightChild

read = lambda : sys.stdin.readline().split()
N = int(input())
Arr = list( map(int, read()) )[::-1]
Tree = [0]*(4*N)
Node, Start, End = 1, 0, N-1

Init(Node, Start, End)
ans = 0

for i in range(1, N):
    K = Arr[i]
    j = Solve(Node, Start, End, 0, i-1)
    #print(j)
    ans += j

print(ans)