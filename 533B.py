n, k = map(int,input().split())
diff = list(map(int, input().split()))
contest = 0
d = {}

for i in diff:
    try:
        d[i] += 1
    except:
        d[i] = 1
    if len(d) == n:
        for j in range(1,n+1):
            d[j] -= 1
            if d[j] == 0:
                del d[j] 
        print("1", end="")
    else:
        print("0", end="")
