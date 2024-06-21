# def noOfCoins(coins,k):
#     dp=[]
#     for i in range(len(coins)):
#         dp.append([0]*(k+1))
#     for i in range(k+1):
#         if i%coins[0]==0:
#             dp[0][i]=i//coins[0]
#         else:
#             dp[0][i]=0
#     i=1
#     while i<len(coins):
#         j=0
#         while j<=k:
#             if j<coins[i]:
#                 dp[i][j]=dp[i-1][j]
#             else:
#                 dp[i][j]=min(1+dp[i][j-coins[i]],dp[i-1][j])
#             j+=1
#         i+=1
#     for i in dp:
#         print(*i)


def fun(coins,k):
    dp=[]
    for i in range(len(coins)):
        dp.append([0]*(k+1))
    for i in range(k+1):
        if i%coins[0]==0:
            dp[0][i]=i//coins[0]
        else:
            dp[0][i]=0
    i=1
    while i<len(coins):
        j=0
        while j<=k:
            if j<coins[i]:
                dp[i][j]=dp[i-1][j]
            if j==coins[i]:
                    dp[i][j]=1
            else: 
                if dp[i][j-coins[i]]<1:
                    dp[i][j]=dp[i-1][j]
                else:
                    if dp[i-1][j]:
                        dp[i][j]=min(1+dp[i][j-coins[i]],dp[i-1][j])
                    else:
                        dp[i][j]=1+dp[i][j-coins[i]]


            j+=1
        i+=1
    for i in dp:
        print(*i)
        
coins=[1,3,4,5]
k=17
#noOfCoins(coins,k)
fun(coins,k)