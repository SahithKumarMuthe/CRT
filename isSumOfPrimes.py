'''for given input N find whether it can be sum of two prime numbers or not using recursion
  IP: 12
  OP: True
  Explanation : 12 is sum of 5 and 7 where 5 and 7 are primes'''
def isprime(n,i=2):
    if n<2:
        return False
    if n==2 or n==3:
        return True
    if n%i==0:
        return False
    if i*i>n:
        return True
    return isprime(n,i+1)
def isSumOfPrimes(n,i=2):
    if n<=4:
        return False
    if n==5:
        return True
    if i==n//2:
        return False
    if isprime(i) and isprime(n-i) and i!=n-i:
        print(i,n-i)
        return True
    return isSumOfPrimes(n,i+1)
    # for i in range(2,n):
    #     print(i,n-i)
    # return False
n=int(input())
print(isSumOfPrimes(n))