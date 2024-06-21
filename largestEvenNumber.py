'''ip : 
    s1= "tu5g2k1h89"
    s2="g5g8gd6h3"
    
  op: 865312
  
  extract unique digits from given string and return maximum even number formed by them'''
def extractDigits(s1,s2):
    l=set()
    for char in s1:
        if char.isdigit():
            l.add(int(char))
    for char in s2:
        if char.isdigit():
            l.add(int(char))
    l=list(l)
    el=[i for i in l if i%2==0]
    ol=[i for i in l if i%2]
    # largestEvenNumber(el,ol)
    fun(l)
def fun(l):
    l.sort(reverse=True)
    if l[-1]%2==0:
        print(''.join(map(str,l)))
    else:
        for i in range(len(l)-2,-1,-1):
            if l[i]%2==0:
                l.append(l.pop(i))
                print(''.join(map(str,l)))
                break
        else:
            print(-1)
# def largestEvenNumber(el,ol):
#     el.sort(reverse=True)
#     ol.sort(reverse=True)
#     num=""
#     i=0
#     j=0
#     while i<(len(el)-1) and j<len(ol):
#         if el[i]>ol[j]:
#             num+=str(el[i])
#             i+=1
#         else:
#             num+=str(ol[j])
#             j+=1
#     while  j<len(ol):
#         num+=str(ol[j])
#         j+=1
#     while i<len(el):
#         num+=str(el[i])
#         i+=1
# print(num)
extractDigits("tu5g2k1h89","g5g8gd6h3")