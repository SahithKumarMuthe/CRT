def threePossibleCombinations(l,k,ans=[],start=0):
    if len(ans)==k:
        print(ans)
        return
    for i in range(start,len(l)):
        threePossibleCombinations(l,k,ans+[l[i]],i+1)
threePossibleCombinations([1,2,3,4,5,6],3)