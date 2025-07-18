a=[1,2,2,3,4,4,5,5,5]
unique=[]
for i in a:
    if i not in unique:
        unique.append(i)
print(unique)
from collections import orderedDict
b=[2,3,4,4,5,5,6,7,7]
print(list(orderedDict.fromkeys(b)))
