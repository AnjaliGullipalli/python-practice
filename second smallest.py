arr1=[1,2,3,4,5]
small=float('inf')
sec_small=float('inf')
for i in arr1:
     if i<small:
        sec_small=small
        small=i
     elif i<sec_small and i!=small:
         sec_small=i
print(sec_small)


