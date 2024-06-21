def iscoprime(n,m):
    for i in range(2,min(n,m)+1):
        if n%i==0 and m%i==0:
            return False
    return True
n=int(input())
m=int(input())
print(iscoprime(n,m))