number = [True]*10005
def Self(n):
    k = n + sum(map(int,list(str(n))))
    if k>10000:
        return
    number[k] = False 
    Self(k)


for i in range(1, 10000):
    Self(i)

for i in range(1,10001):
    if number[i]:
        print(i)

    