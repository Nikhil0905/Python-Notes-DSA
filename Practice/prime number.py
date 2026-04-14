n=int(input("Enter a no. : "))
k=0
if n>1:
    for i in range(2,n):
        if n%i==0:
            k=k+1
    if k==0:
            print("prime")
    else:
            print("not prime")
else:
    print("not prime")