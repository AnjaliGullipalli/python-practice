def fibonacci(n):
    a=0
    b=1
    
    if n<0:
        return 'invalid'
    elif n==1:
        return a
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(10))

def Fibonacci(n):

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(9))

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Print first 10 Fibonacci numbers
fibonacci_sequence(10)
