from collections import Counter
n = int(input())
for i in range(n):
    a = input().lower() 
    b = Counter(a)
    c = 0
    d = sum([len(i) for i in a.split()])
    for i in "aeiou":
        c += b[i]
    print(d-c, c)
