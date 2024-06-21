def isPrime(n):
    if n==2 or n==3 or n==5:
        return True
    if n<2:
        return False
    if n%2==0 or n%3==0:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
def sumOfPrimes(nums):
    ans=0
    for i in range(1,len(nums)):
        prime=0
        for j in range(nums[i]-1,nums[i-1],-1):
            if isPrime(j):
                prime=j 
                break      
        ans+=prime
    return ans          
print(sumOfPrimes([4,8,14,22,36,68]))

