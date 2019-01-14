import sys 

def write(x, y):
    print( "%d %d"%(x, y) )
    sys.stdout.flush()

def read():
    a = sys.stdin.readline().split()
    if len(a) == 3:
        exit()
    for i in range(665):
        sys.stdin.readline() 

x, y = map(int, input().split())
    
while 1:
    read() 
    
    if x < 500:
        x += 1
    if x > 500:
        x -= 1
    if y < 500:
        y += 1
    if y > 500:
        y -= 1
    
    write(x, y)

    if x == 500 and y == 500:
        break 

p = []
for i in range(666):
    a = list(map(int, sys.stdin.readline().split()))
    p.append(a)

p1, p2, p3, p4 = 0,0,0,0

for i in p:
    x, y = i[0], i[1]
    if 1<=x<=499 and 1<=y<=499:
        p1+=1
    elif x>=501 and 1<=y<=499:
        p2+=1
    elif 1<=x<=499 and y>=501:
        p3+=1
    elif x>=501 and y>=501:
        p4+=1

k = [p1, p2, p3, p4]
if min(k) == p1:
    dx, dy = 1, 1
elif min(k) == p2:
    dx, dy = -1, 1
elif min(k) == p3:
    dx, dy = 1, -1
else:
    dx, dy = -1, -1


while 1:
    read()

    x += dx
    y += dy

    write(x, y)
