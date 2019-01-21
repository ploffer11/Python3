mod = 1000000007

dp = [[0]*3 for i in range(200005)]

n, l, r = map(int, input().split())
l3, r3 = l%3, r%3
k = r-l+1

if l3 == r3:	
    zero = k  // 3
    one = k  // 3
    two = k  // 3;
    if ( l3 == 0 ):
        zero+=1
    elif ( l3 == 1 ):
        one+=1
    else:
        two+=1

elif ( l3 == 0 and r3 == 1 ):
    zero, one, two = k  // 3 + 1,k  // 3 + 1,k  // 3
elif ( l3 == 1 and r3 == 2 ):
    zero, one, two = k  // 3, k  // 3 + 1, k  // 3 + 1
elif ( l3 == 2 and r3 == 0 ):
    zero,one,two = k  // 3 + 1, k  // 3, k  // 3 + 1
else:
    zero,one,two = k  // 3, k  // 3, k  // 3;


dp[1][0], dp[1][1], dp[1][2] = zero, one, two
#print(zero, one, two)

for i in range(2, n+1):
    dp[i][0], dp[i][1], dp[i][2] =(
        (dp[i-1][0]*zero + dp[i-1][1]*two + dp[i-1][2]*one)%mod,
        (dp[i-1][0]*one + dp[i-1][1]*zero + dp[i-1][2]*two)%mod,
        (dp[i-1][0]*two + dp[i-1][1]*one + dp[i-1][2]*zero)%mod
    )

print(dp[n][0])