N=int(input())
XOR=0
'''for i in range(1,N+1):
    XOR=XOR^i'''
if N%4==1:
    XOR=1
elif N%4==2:
    XOR=N+1
elif N%4==3:
    XOR=0
else:
    XOR=N

print(XOR)