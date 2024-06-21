def moreThanHalfOccurences(nums):
    '''s=set(nums)
    for num in s:
        if nums.count(num)>(len(nums)//2):
            print(num)
            break'''
    
    c=1
    w=nums[0]
    for i in range(1,len(nums)):
        print(c,w)
        if nums[i]==w:
            c+=1
            
        else:
            if c==0:
                c+=1
                w=nums[i]
            else:
                c-=1
                w=nums[i]
    print(c,w)       
    print(w)

nums=[4,8,2,4,4,8,4]
nums1=[2,1,2,2]
moreThanHalfOccurences(nums)
