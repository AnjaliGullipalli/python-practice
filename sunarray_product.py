arr=list(map(int,input().split()))
if len(arr)<2:
    print("not")
max1 = max2 = float('-inf')
min1 = min2 = float('inf')

    for num in arr:
        if num > max1:
            max2, max1 = max1, num
        elif num > max2:
            max2 = num
        
        if num < min1:
            min2, min1 = min1, num
        elif num < min2:
            min2 = num

if max1*max2>min1*min2:
    print(max1,max2)
else:
    print(min1,min2)
