n=int(input())
stick = list(map(int,input().split()))
d = []

for i in range(1, max(stick)+1):
    s = 0
    for j in stick:
        s += min(abs(i-1-j), abs(i-j), abs(i+1-j))
    d.append((s, i))

d.sort()

print(d[0][1],d[0][0])
