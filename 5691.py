while 1:
    a,b=map(int,input().split())
    if a|b==0:
        exit()
    print(2*a-b)