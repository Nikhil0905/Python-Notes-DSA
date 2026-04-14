# for row in range(7):
#     for col in range(5):
#         if (col==0 and row!=0 and row!=6)or ((row==0 or row==6) and (col>0)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

n=int(input("Vertical: "))
for i in range(1,n):
    print("*",end=" ")
for i in range(1,n):
    print("*")
for i in range(n+1,n*2+1):
    print("*",end=" ")