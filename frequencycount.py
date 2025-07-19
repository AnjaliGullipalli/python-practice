a=[1,2,6,5,4,2,1]
freq={}
for i in a:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
print(freq)


