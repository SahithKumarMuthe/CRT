"""ip:
    chandana:3876,hero:9873,car:789
op:
    aox

explanation:
    consider each pair seperatley
        for chandana:3876
            len(chandana)=8
                8 is present in 3876 so 1st letter of op is last char of chandana
        for hero:9873
            len(hero)=4
                4 not prsent in 9873 so decrement len by 1 -> 3 ,3 is present in 9873 so we have concateneted result with 3rd char in hero
        in the same manner when len reaches to 0 then we concate 'x'
        """




def fun(k,v):
    l=len(k)
    for i in range(l,0,-1):
        if str(i) in v:
            return k[i-1]
    return 'x'
s=""
ip=input().split(",")
for i in ip:
    k,v=i.split(":")
    s+=fun(k,v)
print(s)
