#sum of n natural numbers using recursion
'''def sum(n):
    if n==1:
        return 1
    
    return n+sum(n-1)

print(sum(5))'''

#fibonacci series using recursion
def fib(n):
    global series
    series.append(series[-1]+series[-2])
    if len(series)==n:
        return series
    return fib(n)
series=[0,1]
print(fib(5))


