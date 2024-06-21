def smallestMissingNumber(n,nums):
    '''nums.sort()
    for i in range(n):
        if nums[i]!=i:
            print(i)
            break
    else:
        print(n)'''
    s=n*((n+1)//2)
    print(s-sum(nums))

n=7
nums=[0,5,3,6,4,2,1]
smallestMissingNumber(n,nums)