def isprime(n):
    if n<=1:
        return "NO"
    if n==2 or n==3:
        return "YES"
    for i in range(2,int(n**(0.5)+1)):
        if n%i==0:
            return "NO"
    else:
        return "YES"
n=int(input())
print(isprime(n))