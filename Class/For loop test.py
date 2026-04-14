# n= list(map(int, input("Enter a multiple value: ").split()))
# l=[]
# l.append(n)
# p=len(l)
# for i in range(len(l)):
#     l2=[]
#     if i%2==0:
#         l2.append(i)
#     print(l2)




# To find Palindrome 

# n=input("Enter: ")
# for i in n:
#     if n == n[::-1]:
#         print("Palindrome")
#     else:
#         print("Not a Palindrome")


# To count no. of characters in string

# n="google"
# a="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,"
# c=0
# l1=[]
# l2=[]
# for n in a:
#     if n[]==


# WAP to read a string from user and change all the occurances of first character in the string with "#"

n=input("Enter: ")
f=n[0]
c=""
for i in n:
    if n[0]==i:
        c+="#"
    else:
        c+=i
l=list(c)
l[0]=n[0]  
s=''
for i in l:
    s+=i
print(s)




   