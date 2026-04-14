n=int(input("Enter no. of rows: "))
l1=[]
for i in range(n):
    l2=[]
    for j in range(i+1):
        if j==0 or j==i:
            l2.append(1)
        else:
            l2.append(l1[i-1][j-1]+l1[i-1][j])
    l1.append(l2)
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(l1[i][j],end=" ")
    print()
# # c=len(str(n))
# # print(c)
# # s=0
# # e=n
# # while n>0:
# #     r=n%10
# #     s+=r**c
# #     n=n//10
# # if s==e:
# #     print("Armstrong no.")
# # else:
# #     print("Not a Armstrong no.")
