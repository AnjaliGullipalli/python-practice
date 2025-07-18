a='anjali'
rev=''
for i in range(len(a)-1,-1,-1):
    rev+=a[i]
print(rev)

a=list(a)
i=0
j=len(a)-1
while(i<j):
    a[i],a[j]=a[j],a[i]
    i+=1
    j-=1
a=''.join(a)
print(a)