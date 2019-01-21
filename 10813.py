r=lambda:map(int,input().split())
n,m=r()
a=[i+1 for i in range(n)]
a=[0]+a
for i in range(m):
    l,r=map(int,input().split())
    a[l],a[r]=a[r],a[l]
print(*a[1:])