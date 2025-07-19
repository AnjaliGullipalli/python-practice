s1='listen'
s2='silent'
word={ }
if len(s1)!=len(s2):
    print(False)
for i in s1:
    word[i]=word.get(i,0)+1
for i in s2:
    word[i]=word.get(i,0)-1
for value in word.values():
    if value!=0:
        print(False)
print(True)




