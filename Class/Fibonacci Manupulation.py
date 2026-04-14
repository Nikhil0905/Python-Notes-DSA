n=int(input("Enter a nth number: "))
f1=0
f2=1
f=0
s=0
l1=[]
if n<=10:
    while f<=n:
        print(f)
        f=f1+f2
        f1=f2
        f2=f
        if f==1 or f==5:
            l1.append(f)
else:
    print("No. more than 10")
print("sum:",s)
print(l1)
