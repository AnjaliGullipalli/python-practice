def binary(arr,target):
    i=0
    j=len(arr)-1
    while i<=j:
        mid=(i+j)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            i=mid+1
        else:
            j=mid-1
    return -1
arr=[2,3,4,5,6,71]
target=71
print(binary(arr,target))

