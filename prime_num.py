n=int(input('enter a num:'))
if n<=1:
    print(False)
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print(False)
            break
    else:
        print(True)
      
    