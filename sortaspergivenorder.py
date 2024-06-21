n=int(input())
years=n//360
n=n%360
months=n//30
n=n%30
weeks=n//6
days=n%6
print(f"{years}y-{months}m-{weeks}w-{days}d")