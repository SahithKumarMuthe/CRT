def noOfCoins(coins,k):
    dp=[[0 for _ in range(k+1)] for _ in range(len(coins))]
    for i in range(coins[0]+1):
        if i%coins[0]==0:
            dp[0][i]=1
    for i in range(1,len(coins)):
        j=0
        while j<=k:
            if j<coins[i]:
                dp[i][j]=dp[i-1][j]
            else:
                if dp[i-1][j]:
                    dp[i][j]=dp[i-1][j]
                else:
                    x=j-coins[i]
                    if dp[i-1][x]:
                        dp[i][j]=1
                        
                    
            j+=1
    for i in dp:
        print(i)
    if dp[-1][-1]:
        print("YES")
    else:
        print("NO")           
coins=list(map(int,input().split()))
k=int(input())
noOfCoins(coins,k)
