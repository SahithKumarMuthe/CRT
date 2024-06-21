def noOfHours(n):
    hrs=mins=secs=0
    hrs=n//3600
    n=n%3600
    mins=n//60
    secs=n%60
    print(f"{hrs}h:{mins}m:{secs}s")

n=int(input())
noOfHours(n)