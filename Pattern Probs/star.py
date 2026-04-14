n=int(input("n:"))
for i in range(n):
  for i in range(i,n):
    print(" ",end="")
  for j in range(i+1):
    print("*",end="")  
  print()