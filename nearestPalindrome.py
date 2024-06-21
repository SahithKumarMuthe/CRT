def fun(n):
    l=len(n)//2
    x=n[:l]
    if len(n)%2==1:
        if int(x+str(int(n[l]))+x[::-1])>int(n):
            print(x+str(int(n[l]))+x[::-1])
        else:
            print(x+str(int(n[l])+1)+x[::-1])
    else:
        if int(x+x[::-1])>int(n):
            print(x+x[::-1])
        else:
            x=str(int(x)+1)
            print(x+x[::-1])
n=input()
fun(n)