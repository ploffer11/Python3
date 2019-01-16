import sys
read = lambda : map(int, sys.stdin.readline().split())
write = sys.stdout.write

def init(node, start, end):
    global arr, tree 
    
    if start == end:
        here = start 
        tree[node] = arr[here]
        return tree[node]
    
    mid = (start + end) // 2
    leftchild, rightchild = (
        init(node*2, start, mid), init(node*2 + 1, mid+1, end)
    )
    tree[node] = leftchild + rightchild 
    return tree[node]

def update_lazy(node, start, end):
    global tree, arr, lazy
    if lazy[node] != 0:
        tree[node] += (end-start+1)*lazy[node]
        if (start != end):
            lazy[node*2] += lazy[node]
            lazy[node*2 + 1] += lazy[node]
        lazy[node] = 0

def tree_sum(node, start, end, left, right):
    global tree, arr, lazy

    update_lazy(node, start, end)
    
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    leftchild, rightchild = (
        tree_sum(2*node, start, mid, left, right), tree_sum(2*node + 1, mid+1, end, left, right)
    )

    return leftchild + rightchild 

def update(node, start, end, left, right, diff):
    global tree, arr, lazy  

    update_lazy(node, start, end)

    if start > right or end < left:
        return

    if left <= start and end<=right:
        tree[node] += (end-start+1) * diff
        if (start != end):
            lazy[node*2] += diff
            lazy[node*2 + 1] += diff
        return 

    mid = (start + end) // 2 
    update(2*node, start, mid, left, right, diff)
    update(2*node+1, mid+1, end, left, right, diff)
    tree[node] = tree[node*2] + tree[node*2 + 1]


n, m, k = read() 
arr = []
tree = [0] * (4*n)
lazy = [0] * (4*n)

for _ in range(n):
    arr += [int(sys.stdin.readline())]

init(1, 0, n-1)

for _ in range(m+k):
    #print (tree)
    a = list(read())
    if len(a) == 4:
        trash, left, right, diff = a
        left, right = left-1, right-1
        update(1, 0, n-1, left, right, diff)


    else:
        trash, left, right = a
        left, right = left-1, right-1
        write(f"{tree_sum(1, 0, n-1, left, right)}\n")