a=[1,6,5,3,3,2,1]
seen=set()
unique=[]
for i in a:
    if i not in seen:
        seen.add(i)
        unique.append(i)
print(unique)