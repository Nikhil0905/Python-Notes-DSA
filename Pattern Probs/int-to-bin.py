n=int(input("Enter Integer: "))
c=''
while n>0:
    r=n%2
    c+=str(r)
    n=n//2
print(c[::-1])