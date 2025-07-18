a=[1,2,3,4,5,6]
a.sort()
n=len(a)
mid=n//2
if n%2==1:
    print(a[mid])
else:
    print((a[mid-1] + a[mid]) / 2)