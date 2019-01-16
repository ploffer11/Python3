import bisect

n = int(input())
arr = map(int, input().split())
b = [n+1]
ans = 0

for i in reversed(list(arr)):
    k = bisect.bisect_left(b, i)
    b[k:k+1] = [i,b[k]]
    ans += k

print (ans) 