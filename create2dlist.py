# def create2dlist(l,ans=[]):
#     res=[]
#     for i in l:
#         if i not in res:
#             res.append(i)
#         else:
#             print(res)
#             ans.append(res)
#             res=[]
#             res.append(i)
#     print(res)
#     ans.append(res)
#     return ans

# print(create2dlist([2,3,1,3,4,3,2]))

def create2dlist(l,ans=[]):
    res=[]
    for num in l:
        if num not in res:
            i=0
            while i <len(ans):
                if num not in ans[i]:
                    ans[i].append(num)
                    break
                i+=1 
            else:
                res.append(num)      
        else:
            ans.append(res)
            res=[]
            res.append(num)
    ans.append(res)
    return ans

print(create2dlist([1,1,1,1,1,1,1]))