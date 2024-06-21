l=list(map(int,input().split()))
left=l[0]
right=l[-1]
mrng=1
evng=1
for i in range(1,len(l)):
    if l[i]>left:
        left=l[i]
        mrng+=1
for i in range(len(l)-2,-1,-1):
    if l[i]>right:
        right=l[i]
        evng+=1
print(mrng,evng)
