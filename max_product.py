def max_product(arr1):
    arr1.sort()
    return max(arr1[-1]*arr1[-2],arr1[0]*arr1[1])
arr1 = [1, -2, 3, -4, 5]
print(max_product(arr1))


            
    
