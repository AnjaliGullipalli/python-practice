a=[2,4,5,6,7]
left=0
right=len(a)-1
while left<right:
    a[left],a[right]=a[right],a[left]
    left+=1
    right-=1
print(a)
a1=[4,6,2,3,1]
a2=a1[::-1]
print(a2)
a3=[1,2,3,4]
a3.reverse()
print(a3)