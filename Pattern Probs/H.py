n=int(input("Enter Size: "))
m=int(n/2)
for i in range(n):
    for j in range(n-2):
        if j==0 or j==(n-3) or (i==m and (j>0 and j<(n-3))):
            print("*",end="")
        else:
            print(end=" ")
    print()