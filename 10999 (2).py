import sys
read = lambda : map(int, sys.stdin.readline().split())
write = sys.stdout.write

class SegmentTree:
    def __init__(self, n):
        self.tree, self.lazy, self.arr, self.n =(
            [0] * (4*n), [0] * (4*n), [], n
        ) 
    
    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return self.tree[node]
        else:
            mid = (start + end) // 2
            self.tree[node] = (
                self.init(node*2, start, mid) +
                self.init(node*2 + 1, mid+1, end)
            )
            return self.tree[node]

    def lazy_propagation(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node*2] += self.lazy[node]
                self.lazy[node*2 + 1] += self.lazy[node]
            self.lazy[node] = 0
    
    def tree_sum(self, node, start, end, left, right):
        self.lazy_propagation(node, start, end)

        if start > right or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        leftchild, rightchild = (
            self.tree_sum(2*node, start, mid, left, right), 
            self.tree_sum(2*node + 1, mid+1, end, left, right)
        )

        return leftchild + rightchild 

    def update(self, node, start, end, left, right, diff):
        self.lazy_propagation(node, start, end)

        if start > right or end < left:
            return

        if left <= start and end <= right:
            self.tree[node] += (end - start + 1) * diff
            if start != end:
                self.lazy[2 * node] += diff
                self.lazy[2 * node + 1] += diff
            return

        mid = (start + end) // 2
        self.update(node*2, start, mid, left, right, diff)
        self.update(2*node+1, mid+1, end, left, right, diff)
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1] 
    
n, m, k = read()
node, start, end = 1, 0, n-1
segment_tree = SegmentTree(n)

for i in range(n):
    segment_tree.arr += [int(sys.stdin.readline())]

segment_tree.init(node, start, end)



for i in range(m + k):
    a = list(read())

    if a[0] == 1:
        segment_tree.update(node, start, end, a[1]-1, a[2]-1, a[3])
    else:
        write(
            f"{segment_tree.tree_sum(node, start, end, a[1]-1, a[2]-1)}\n"
        )

