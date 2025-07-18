a=list(map(int,input().strip("[]").split(',')))
a.sort()
mid=len(a)//2
first_half=a[:mid]
sec_half=a[mid:]
sec_half.reverse()
print(first_half+sec_half)

