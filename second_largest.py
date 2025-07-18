arr1=[2,4,3,5]
largest=float('-inf')
second_largest=float('-inf')
for i in arr1:
    if i > largest:
        second_largest=largest#2,
        largest=i#2,4
    elif i > second_largest and i!=largest:
        second_largest=i
print(second_largest)



