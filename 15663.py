from itertools import product
from itertools import combinations_with_replacement

n, m = map(int,input().split())
arr = set(map(int,input().split()))
ans = []

#for i in product(arr, repeat=m):
    #ans.append(i)

for i in combinations_with_replacement(arr, m):
    ans.append(i)

#print(sorted(ans))
ans2=[]
for i in ans:
    ans2.append(sorted(i))

for i in sorted(ans2):
    print(*i)
