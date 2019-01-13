n, k = map (int, input().split())
arr = list(map(int, input().split()))
arr2 = arr[:]

ans = 0
for i in range(k):
    arr2 = arr[:]
    while i<=n-1:
        arr2[i] = 0
        i += k
    e, s = arr2.count(1), arr2.count(-1) 
    ans = max(ans, abs(e-s))

print (ans)

