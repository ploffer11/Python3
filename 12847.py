n, m = map(int,input().split())
t = list(map(int,input().split()))
s = [0, t[0]]

for i in range(1,n):
    s.append(s[-1]+t[i])

ans = -1

for i in range(m, n + 1):
    ans = max(ans, s[i] - s[i-m])

print(ans)