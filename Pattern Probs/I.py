n=int(input("Size: "))
e=int(n/2)
o=int((n+1)/2)
print(o)
if n%2!=0:
    for i in range(n):
        for j in range(n-2):
            if j==o or (i==0 or i==n-1) and j!=o :
                print("*",end="")
            else:
                print(end=" ")

else:
    for i in range(n):
        for j in range(n-2):
            if j==e or (i==0 or i==n-1) and j!=e :
                print("*",end="")
            else:
                print(end=" ")