import sys
import itertools
from collections import namedtuple

read = lambda : tuple(map(int, sys.stdin.readline().split()))

Vector = namedtuple("Vector", "x y point")

class Coordinate:
    def __init__(self):
        self.n, self.point = (
            4, []
        )

        for i in range(self.n):
            self.point.append(read())

        self.point = list(set(self.point))
        self.n, self.check= (
            len(self.point), {i : True for i in self.point}
        )

    def square_check(self, idx):
        k = 0
        vector = [
            Vector(
                i[0]-self.point[idx][0],
                i[1]-self.point[idx][1],
                (i[0], i[1])
            ) for i in self.point if (
                i[0]!=self.point[idx][0] or i[1]!=self.point[idx][1]
            )
        ]
        for i in itertools.combinations(vector, 2):
            vector1, vector2 = i
            if not self.inner_product(vector1, vector2) and (
                self.square_size(vector1) == self.square_size(vector2)):
                x, y = (
                    vector1.point[0] + vector2.x,
                    vector1.point[1] + vector2.y
                )
                if self.check.get((x, y), False):
                    k = max(k, self.square_size(vector1))
        return k
                
    def inner_product(self, vt1, vt2):
        return (
            vt1.x * vt2.x + vt1.y * vt2.y
        )

    def square_size(self, vt):
        return (
            vt.x*vt.x + vt.y*vt.y
        )

    def solve(self):
        ans = 0
        ans = max(ans, self.square_check(0))
        if ans:
            print(1)
        else:
            print(0)



t = int(input())
for _ in range(t):
    s = Coordinate()
    s.solve()

