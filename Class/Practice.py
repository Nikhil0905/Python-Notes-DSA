a=0
n=a
l1=[]
l2=[]
l3=[]
print("Enter -1 to exit:")
if n==-1:
    exit   
while n!=-1:
    a=int(input("Enter any number: "))
    if a==1:         
        continue       
    elif a==0:
        l3.append(a) 
        continue     
    elif a>0:
        l1.append(a)
        continue
    elif a<0 and a!=-1:
        l2.append(a)
        continue
    else:
        break
print("Number of Positive numbers:",len(l1))
print("Number of Negative numbers:",len(l2))
print("Number of zeros:",len(l3))