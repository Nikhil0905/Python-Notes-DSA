n=int(input("Enter no of rows: "))
for i in range(0,n):   #rows
    for j in range(i,n):   #columns
        print(" ",end=" ")
    for j in range (0,i-1):                            #for upper triangle 
        print("*",end=" ")
    for j in range (0,i):
        print("*",end=" ")
    print()
for i in range(0,n+1):
    for j in range(i):
        print(" ",end=" ")
    for j in range (i,n-1):                            #for lower triangle
        print("*",end=" ")
    for j in range (i,n):
        print("*",end=" ")
    print()