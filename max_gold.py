def max_gold(l):
    if not l:
        return 
    if len(l)==1:
        return l[0]
    if len(l)==2:
        return max(l)
    if len(l)==3:
        return max(l[0]+l[2],l[1])
    l_sum=l[0]+max_gold(l[2:])
    r_sum=l[1]+max_gold(l[3:])

    return max(l_sum,r_sum)
l=list(map(int,input().split(" ")))
print(max_gold(l))