def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        mergesort(left)
        mergesort(right)
        merge(arr,left,right)

def merge(arr,left,right):
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        k+=1
        j+=1

my_list=[64,34,25,12,22,11,90]

print(f"Orginal list : {my_list}")
mergesort(my_list)
print(f"Sorted list : {my_list}")

