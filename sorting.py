a=[2,4,1,6,8,1]
i=0 
j=len(a)-1
while(i<j):
    if a[i]<a[j]:
        a[i],a[j]=a[j],a[i]
        i+=1
        j-+1
print(a)

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(arr)
