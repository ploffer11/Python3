import sys
read = lambda : map(int,sys.stdin.readline().split())
write = sys.stdout.write

class SegmentTree:
    def __init__(self, n):
        self.tree, self.arr, self.n, self.mod = (
            [0] * (4*n), [0]*n, n, 1000000007
        )
        for i in range(n):
            self.arr[i] = int(sys.stdin.readline())


    def check(self, start, end, left, right):
        return (start > right or end < left)
    
    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.init(node*2, start, mid)
            self.init(node*2+1, mid+1, end)
            self.tree[node] = (
                (self.tree[node*2] * self.tree[node*2+1])
            ) % self.mod
    
    def tree_multiple(self, node, start, end, left, right):
        if self.check(start, end, left, right):
            return 1
        
        if left <= start and end <= right:
            return self.tree[node]

        if start != end:
            mid = (start + end) // 2
            return (
                self.tree_multiple(2*node, start, mid, left, right) *
                self.tree_multiple(2*node+1, mid+1, end, left, right)
            ) % self.mod
        
    
    def update(self, node, start, end, index, num_from, num_to):

        if not start <= index <= end:
            return

        if start == end:
            try:
                self.tree[node] //= num_from
            except:
                self.tree[node] = 1
            self.tree[node] *= num_to
        else:
            mid = (start + end) // 2
            self.update(2*node, start, mid, index, num_from, num_to)
            self.update(2*node+1, mid+1, end, index, num_from, num_to)
            self.tree[node] = (
                self.tree[node*2] * self.tree[node*2 +1]
                ) % self.mod 
        


n, m, k = read()
node, start, end = 1, 0, n-1
segment_tree = SegmentTree(n)
segment_tree.init(node, start, end)

for j in range(m+k):
    #print(segment_tree.tree)
    a, b, c = list(read())
    if a == 1:
        segment_tree.update(node, start, end, b-1, segment_tree.arr[b-1], c)
        segment_tree.arr[b-1] = c
    else:
        write("{}\n".format(
            segment_tree.tree_multiple(node,start,end,b-1,c-1) %
            segment_tree.mod
        ))