class Trie:
    def __init__(self):
        self.alpha={}
        self.count=0
        self.f=0
    def insert(self,word):
        t=self
        for char in word:
            if char in t.alpha:
                t=t.alpha[char]
                t.count+=1
            else:
                t.alpha[char]=Trie()
                t=t.alpha[char]
                t.count=1
        t.f=1
    def search(self,word):
        t=self
        for char in word:
            if char not in t.alpha:
                return 0
            t=t.alpha[char]
        return t.f
    def prefix(self,word):
        t=self
        for char in word:
            if char not in t.alpha:
                return 0
            t=t.alpha[char]
        return t.count
    def delete(self,word):
        t=self
        for char in word:
            t=t.alpha[char]
            t.count-=1
        t.f=0
    def allPrefixes(self,word):
        def words(s1,t,max,len,ms):
            if t.f==1:
                print(s1)
                if len>max:
                    max=len 
                    ms=s1
                elif len==max:
                    if ms>s1:
                        ms=s1
            for i in t.alpha:
                max,ms=words(s1+i,t.alpha[i],max,len+1,ms)
            return max,ms 
        t=self
        s1=""
        len=0
        for char in word:
            if char in t.alpha:
                t=t.alpha[char]
                s1+=char
                len+=1
            else:
                return 0,""
        max,ms=words(s1,t,0,len,"")
        return max,ms               
t=Trie()
t.insert("word")
t.insert("world")
t.insert("apple")
t.insert("apricot")
queries=list(input().split())
i=0
s=("","")
for query in queries:
    m,ts=t.allPrefixes(query)
    if m==i:
        if s[0]>query:
           s=(query,ts)
    elif m>i:
        i=m
        s=(query,ts)
print(i,s)
n=int(input())
for i in range(n):
    m,s=input().split()
    if m=="1":
        t.insert(s)
    elif m=="2":
        print(t.search(s))
    elif m=="3":
        print(t.prefix(s))
    elif m=="4":
        t.delete(s)
    else:
        print(t.allPrefixes(s))



    
    