import itertools as it
read = lambda : map(int, input().split())
n, m = read()
a = [list(read()) for i in range(n)]
ans = 0
for j in it.combinations(list(range(m)), 3):
    s = 0
    for i in range(n):
        s += max(a[i][j[0]], a[i][j[1]], a[i][j[2]])
    ans = max(s, ans)
print(ans)
