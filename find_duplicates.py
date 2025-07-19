a=[1,1,2,5,7,3,4,4,3]
freq={}
for i in a:
    freq[i]=freq.get(i,0)+1 #{1:2,2:1.5:1,7:1,3:2,4:2}
print(freq)
repeating=[]
for i,count in freq.items():#([(4, 3), (2, 2), (5, 1), (3, 2), (1, 1)]))
    if count>1:
        repeating.append(i)
print(repeating)





