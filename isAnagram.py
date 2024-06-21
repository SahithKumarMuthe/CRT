def rotate(s,q,n):
    if q=='R':
        return s[-n]
    else:
        return s[n]
def isanagram(s,res,nqueries):
    i=0
    j=i+nqueries
    while j<len(s):
        print(sorted(s[i:j]))
        print(sorted(res))
        if sorted(s[i:j])==sorted(res):
            return True
        i+=1
        j+=1
    return False

s=input()
nqueries=int(input())
res=''
for i in range(nqueries):
    q,n=input().split(" ")
    char=rotate(s,q,int(n))
    res=res+char
print(isanagram(s,res,nqueries))