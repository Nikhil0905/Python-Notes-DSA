n=int(input("n: "))  #no. of rows
list1=[]    #vacant list
for i in range(n):  #for rows ofn list
    l2=[]
    for j in range(i+1):  #for column of list
        if j==0 or j==i:
            l2.append(1)
        else:
            l2.append(list1[i-1][j-1]+ list1[i-1][j])
    list1.append(l2)

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(list1[i][j],end=" ")  
    print()      
