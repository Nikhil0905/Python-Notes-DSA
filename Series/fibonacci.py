n= int(input("Enter No. of terms: "))
f1=0
f2=1
i=0
if n==0:
    print("")
elif n==1:
    print(f1)
elif n==2:
    print(f1)
    print(f2)
else:
    while i<n:
        print(f1)
        f=f1+f2
        f1=f2
        f2=f
        i+=1
    print()