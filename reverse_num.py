num=1234
reverse=0
while num>0:
    reverse=reverse*10+num%10
    num=num//10
print(reverse)

n=1234
n1=int(str(n)[::-1])
print(n1)