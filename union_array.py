#using brute force
def get_union(a,b):
    merge=a+b
    unique=set(merge)
    return sorted(unique)
a=[1,2,3,3,4,5,6]
b=[3,4,4,5,6,7,]
print(get_union(a,b))