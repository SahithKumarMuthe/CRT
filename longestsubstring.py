# def longestSubString(s):
#     max_l=0
#     for i in range(len(s)):
#         j=i+1
#         while j<(len(s)-1):
#             if len(set(s[i:j+1]))==len(s[i:j+1]):
#                 l=len(s[i:j+1])
#                 if l>max_l:
#                     max_l=l
#             j+=1
#     return max_l
# s=input()
# print(longestSubString(s))
    
def longestSubString(s):
    max_l=0
    res=""
    i=0
    while i<len(s):
        j=i+1
        res+=s[i]
        while j<(len(s)):
            if s[j] in res:
                max_l=max(max_l,len(res))
                res=""
                break
            else:
                res+=s[j]
                print(res)
                j+=1
        i=s.index(s[i:j+1])+1
    return max_l
s=input()
print(longestSubString(s))
    
