def left_roation(a):
    if not a:
        return []
    temp=a[0]
    for i in range(len(a)-1):
        a[i]=a[i+1]
    a[-1]=temp
    return a
a=[1,2,3,4,5]
print(left_roation(a))
