n=int(input("Enter a number: "))
c=len(str(n))
e=n
s=0
while n>0:
    r=n%10
    s+=r**c
    n//=10
if e==s:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
print()
