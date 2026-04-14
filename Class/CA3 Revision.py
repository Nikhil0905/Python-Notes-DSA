              # Triange With @ at (i==0 and j==4) and at (i==4 and j==0)

n=7
for i in range(n):
    for j in range(n):
        if (i==0 and j==0) or (i==6 and j>=0)  or (j==0 and i>4) or (j==0 and i<4) or (i==1 and j==1) or (i==2 and j==2) or (i==3 and j==3) or (i==5 and j==5) or (i==6 and j==6) :
            print("*",end="  ")
        elif (i==4 and j==4) or (i==4 and j==0):
            print("@",end=" ")
        else:
            print(" ",end="  ")
    print()

            
           # Take inputs acc. to User

l=list(map(str,input("Enter only 5 elements: ").split(" ")))
if len(l)==5:
    print("You have entered 5 elements")
else:
    print("Enter elements less than 5.", "You have entered",len(l),"elements")

                # Triangle with pattern

n=7
for i in range(n):
    for j in range(n):
        if (i==0 and j==0) or (i==6 and j>0)  or (j==0 and i>0) or (i==1 and j==1) or (i==2 and j==2) or (i==3 and j==3) or (i==4 and j==4) or (i==5 and j==5) or (i==6 and j==6) :
            print("*",end="  ")
        else:
            print(" ",end="  ")
    print() 

                # Multiplication and Addition

class A():
    def __init__(self,n,m):
        self.n=n
        self.m=m
    def add(self):
        print(self.n+self.m)
class B(A):
    def mult(self):
        print(self.n*self.m)
c1=B(5,5)

c1.add()
c1.mult()