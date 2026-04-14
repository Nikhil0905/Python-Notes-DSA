r=int(input("rows: "))
c=int(input("coloumn: "))
l1=[]
print("row wise elements:")
for i in range(r):
    x=list(map(int,input().split()))
    l1.append(x)
print("matrix is",l1)
lt=[]
for i in range(c):
    li=[]
    for j in range (r):
        li.append(l1[j][i])
    lt.append(li)
   
print("transpose",lt)
