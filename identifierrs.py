a=10
print(id(a))
a=20
print(id(a))
print(a)


name='chandana'
print(name[::2])
b=bin(57)
print(int(b,2))
name='chandana'
print(id(name))
name='pingili chandana'
print(id(name))
l1=[1,2]
print(id(l1))
l1=[1,2,3]
print(id(l1))
l2=l1
l2=[4,5,6]
print(id(l2))
l1=[7,8,9]
print(l1)
print(l2)
