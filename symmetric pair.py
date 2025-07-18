#A symmetric pair is a pair (a, b) such that its reverse (b, a) also exists in the array.
a1=[(1,2),(3,4),(6,7),(2,1),(7,6),(0,1),(0,1)]
seen=set()
s=[]
for a,b in a1:
    if (b,a) in seen:
        s.append((a,b))# then store in s
    seen.add((a,b)) #first it store pairs
print(s)
