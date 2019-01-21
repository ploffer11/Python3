N, C = map(int, input().split())
arr = list(map(int, input().split()))
d = {}

for i in range(N):
    try:
        d[arr[i]][0] += 1
    except:
        d[arr[i]] = [1, N-i]

arr = []

for key, value in d.items():
    arr.append([
        value[0], value[1], key 
    ])

arr.sort()

for i in arr[::-1]:
    for j in range(i[0]):
        print(i[2], end=" ")