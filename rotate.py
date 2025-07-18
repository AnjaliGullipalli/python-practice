a=[1,2,3,4,5,6,7]
k=3
k=k%len(a)
a[:k]=reversed(a[:k])
a[k:]=reversed(a[k:])
a[:]=reversed(a)
print(a)