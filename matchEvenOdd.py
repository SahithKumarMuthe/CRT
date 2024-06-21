def matchEvenOdd(nums1,nums2):
    def addOdd(n,nums2):
        if not nums2:
            return 
        if nums2[0]%2==1:
            res.append(n+nums2[0])
        addOdd(n,nums2[1:])
    if not nums1:
        return 
    if nums1[0]%2==0:
        addOdd(nums1[0],nums2)
    matchEvenOdd(nums1[1:],nums2)

def matchEvenOdd2(nums1,nums2):
    def addOdd2(n,nums2,ans):
        if not nums2:
            return ans 
        if nums2[0]%2==1:
            ans+=nums2[0]+n
        return addOdd2(n,nums2[1:],ans)
    if not nums1:
        return 
    if nums1[0]%2==0:
        ans=addOdd2(nums1[0],nums2,0)
        res.append(ans)
    return matchEvenOdd2(nums1[1:],nums2)

nums1=[6,3,2,9,4,7]
nums2=[8,7,5,3,6,9]
res=[]
matchEvenOdd(nums1,nums2)
print(res)
res.clear()
matchEvenOdd2(nums1,nums2)
print(res)