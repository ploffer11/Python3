class SegmentTree:
    def __init__(self):
        self.n = int(input())
        self.arr = list(map(int,input().split()))
        self.tree = [ [] for i in range(4*self.n) ]
        self.ans = 0 

    def merge(self, a, b):
        merged, i, j = [], 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                self.ans += len(a) - i
                j += 1
        if i == len(a):
            merged += b[j:]
        else:
            merged += a[i:]
    
        return merged

    def init(self, node, start, end):
        if start == end:
            self.tree[node] = [ self.arr[start] ]
        else:
            mid = (start + end) // 2
            self.init(node*2, start, mid)
            self.init(node*2+1, mid+1, end)
            self.tree[node] = self.merge(
                self.tree[node*2], self.tree[node*2 + 1]
                )

S = SegmentTree()
S.init(1, 0, S.n - 1)
print (S.ans)