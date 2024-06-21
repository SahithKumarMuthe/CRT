def minNoOfCoins(coins,k):
    c=0
    coins.sort()
    for i in range(len(coins)-1,-1,-1):
        print(k)
        if k%coins[-i]==0:
            c+=k//coins[i]
            break
        else:
            c+=k//coins[i]
            k=k%coins[i]
        if k==0:
            break
    print(c)

coins=[4,3,7]
k=16
minNoOfCoins(coins,k)