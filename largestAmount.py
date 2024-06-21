'''in given word matrix check whether given string is prsent or not

ip : 
    e t o f
    e a l m
    o g l x
    w e r t

    tall
OP: True'''
def isStringPresent(s,i,j,flag=False,k=1):
    print(s,i,j)
    if i<0 or j<0 or i>=n or j>=n:
        return
    if len(s)==k:
        flag=True
        return flag
    if words[i][j]==s[k]:
        words[i][j]='-'
    if not flag:
        flag=isStringPresent(s,i-1,j,flag,k+1)
        flag=isStringPresent(s,i,j-1,flag,k+1)
        flag=isStringPresent(s,i+1,j,flag,k+1)
        flag=isStringPresent(s,i,j+1,flag,k+1)

    return flag
n=int(input())
words=[]
for i in range(n):
    w=input().split(" ")
    words.append(w)

s=input()
Flag=False
for i in range(len(words)):
    for j in range(len(words[i])):
        if words[i][j]==s[0]:
            f=isStringPresent(s,i,j)
            if f:
                Flag=f

print(Flag)