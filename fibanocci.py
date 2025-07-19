def fibanocci(n):
    a,b=0,1
    if n==0:
        return a
    if n==0 or n==1:
        return b
    else:
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return b
print(fibanocci(8))

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(8))


n1=int(input('enter a num:'))
a,b=0,1
for _ in range(n1):
    print(a,end=' ')
    a,b=b,a+b

