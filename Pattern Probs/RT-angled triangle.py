# n=int(input("Enter no of rows: "))
# for i in range(n+1):
#     for j in range (i):
#         print("*",end=" ")
#     print()

n=int(input("rows: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()