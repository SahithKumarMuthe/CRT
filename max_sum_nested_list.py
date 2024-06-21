N=int(input())
L=[]
for i in range(N):
    sub_list=list(map(int,input().split()))
    L.append(sub_list)
max_sum=0
index=0
for i  in range(len(L)):
    l_sum=sum(L[i])
    if l_sum>max_sum:
        max_sum=l_sum
        index=i
print(i)
