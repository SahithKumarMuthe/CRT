arr=[1,2,3,4,5]
key=4
strt,end=0,len(arr)-1
ans=-1
while strt<=end:
    mid=strt+(end-strt)//2
    print(arr[mid])
    if arr[mid]==key:
        ans=mid
        end=mid-1
    elif key>arr[mid]:
        strt=mid+1
    else:
        end=mid-1
print("ans : ",ans)
    
