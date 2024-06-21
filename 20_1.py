d=[1,2,3,4]
d=dict.fromkeys(d,10)
print(d)
d.setdefault(5,100)
print(d)
del d
print(d)

#add keys to dictionary

n=int(input())
d={}
for i in range(n):
    k_v_pair=tuple(map(int,input().split(":")))
    d[k_v_pair[0]]=k_v_pair[1]
print(d)

#check whether a given key already exists in a dictionary.

n=int(input())
d={}
for i in range(n):
    k_v_pair=tuple(map(int,input().split(":")))
    d[k_v_pair[0]]=k_v_pair[1]

key=int(input("key to check : "))
if key in d:
    print("Key is present in dictionary")
else:
    print("Key is not present in the dictionary")

#dictionary with squares upto n

n=int(input())
d1={k:v*v for k, v in enumerate(range(1,n+1),start=1)}
print(d)

#merging two dictionaries
n1=int(input())
d1={}
for i in range(n1):
    k_v_pair=tuple(map(int,input().split(":")))
    d1[k_v_pair[0]]=k_v_pair[1]
print("d1 : ",d1)

n2=int(input())
d2={}
for i in range(n2):
    k_v_pair=tuple(map(int,input().split(":")))
    d2[k_v_pair[0]]=k_v_pair[1]
print("d2 : ",d2)
d3=d1.copy()
d3.update(d2)
print(d3)

# removing kwy from the dictionary
n1=int(input())
d1={}
for i in range(n1):
    k_v_pair=tuple(map(int,input().split(":")))
    d1[k_v_pair[0]]=k_v_pair[1]
print(d1)

n=int(input())
d1.pop(n)
print(d1)

#mapping two lists into a dictionary

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
d={}
for k,v in zip(l1,l2):
    d[k]=v
print(d)#dict(zip(l1,l2))

#combine two dictionaries and adding values for common keys


n1=int(input())
d1={}
for i in range(n1):
    k_v_pair=tuple(map(int,input().split(":")))
    d1[k_v_pair[0]]=k_v_pair[1]
print("d1 : ",d1)

n2=int(input())
d2={}
for i in range(n2):
    k_v_pair=tuple(map(int,input().split(":")))
    d2[k_v_pair[0]]=k_v_pair[1]

d3=d1.copy()

for k,v in d2.items():
    if k in d3:
        d3[k]+=v
    else:
        d3[k]=v
print(d3)