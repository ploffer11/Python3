for i in range(int(input())):
    a=input()
    l=len(a)//2
    if a[l] == a[l-1]:
        print("Do-it")
    else:
        print("Do-it-Not")

exec('a=input();l=len(a)//2;print("Do-it"+"-Not"*(a[l]!=a[l-1]));'*int(input()))