import sys
read = lambda : int(sys.stdin.readline())
write = sys.stdout.write

class SegmentTree:
    def __init__(self):
        self.n = int(input())
        self.arr = []
        for _ in range(self.n):
            self.arr.append(read())
        self.tree, self.node, self.start, self.end =(
            [ [] for i in range(4*self.n) ],
            1,
            0,
            self.n-1
        )

    def merge(self, left_list, right_list):
        merged, i, j = (
            [], 0, 0
        )

        while i!=len(left_list) and j!=len(right_list):
            if left_list[i][0] < right_list[j][0]:
                merged.append(left_list[i])
                i += 1
            else:
                right_list[j][1] += len(left_list) - i 
                merged.append(right_list[j])
                j += 1

        merged+=left_list[i:]
        merged+=right_list[j:]

        return merged 

    def init(self, node, start, end):
        if start == end:
            self.tree[node] = [ [self.arr[start], 1, start] ]
        else:
            mid = (start + end) // 2
            self.init(2*node, start, mid)
            self.init(2*node+1, mid+1, end)
            self.tree[node] = self.merge(
                self.tree[2*node], self.tree[2*node+1]
            )

    def solve(self):
        ans = [0] * self.n
        self.init(self.node, self.start, self.end)
        for i in self.tree[1]:
            ans[i[2]] = i[1]
        
        for j in ans:
            write(f"{j}\n")

segment_tree = SegmentTree()
segment_tree.solve()

