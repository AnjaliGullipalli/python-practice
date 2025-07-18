num=int(input())
order=len(str(num))
sum=0
t=n
while t>0:
    digit=t%10
    sum+=digit**order
    t//=10
if num==sum:
    print(num)
else:
    print(num)


