def max_product(arr1,k):
    if not arr1:
        return 0
    max_len=0
    for i in range(len(arr1)):
        sum=0
        for j in range(i,len(arr1)):
            sum+=arr1[j]
            curr_len=j-i+1
            if sum==k:
                max_len=max(max_len,curr_len)
    return max_len
arr1 = [1,-2,3,-4,5]
k = 5
print(max_product(arr1, k))
           
            
    
