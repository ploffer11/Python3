n, k = map(int,input().split())
string = input()

d = {}

s = 1
if k == 1:
    for i in string:
        try:
            d[i] += 1
        except:
            d[i] = 1
else:
    for i in range(1, n):
        if string[i-1] == string[i]:
            if s<=0:
                s+=2
            else:
                s+=1

        else:
            s = 0

        if s == k:
            if i+1<n and string[i]==string[i+1]:
                s = -1
            else:
                s = 0
            try:
                d[string[i]] += 1
            except:
                d[string[i]] = 1

ans = 0
for i, j in d.items():
    ans = max(ans, j)

print(ans)