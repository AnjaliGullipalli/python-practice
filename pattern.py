n=['A','B','C','D','E']
row=len(n)
for i in range(row):
    for j in range(i,row):
        print(" ", end=" ")
    for j in range(1+i):
        print(n[j], end=" ")
    print()