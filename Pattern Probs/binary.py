n=(input("Enter binary Number: "))
l1=[]
k=0
m=0
for i in n[::-1]:
    i=int(i)
    m=m+(i*2**k)
    k=k+1
print(m,end="")



