def sort3(nums):
    # for i in range(len(nums)-2):
    #     a,b,c=nums[i],nums[i+1],nums[i+2]
    #     if a>b and a>c:
    #         nums[i+2]=a
    #         if b>c:
    #             nums[i+1]=b
    #             nums[i]=c
    #         else:
    #             nums[i+1]=c
    #             nums[i]=b
    #     elif b>c and b>a:
    #         nums[i+2]=b
    #         if c>a:
    #             nums[i+1]=c
    #             nums[i]=a
    #         else:
    #             nums[i+1]=a
    #             nums[i]=c
    #     else:
    #         nums[i+2]=c
    #         if a>b:
    #             nums[i+1]=a
    #             nums[i]=b
    i=0
    while i<len(nums)-2:
        if nums[i]>nums[i+1]:
            nums[i+1],nums[i]=nums[i],nums[i+1]
        elif nums[i+1]>nums[i+2]:
            nums[i+1],nums[i+2]=nums[i+2],nums[i+1]
        else:
            i+=1

nums=list(map(int,input().split()))
print(nums)
sort3(nums)
print(nums)