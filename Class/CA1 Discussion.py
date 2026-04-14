# a="Adkjsfzv"
# for i in a:
#     print(ord(i))
x=input("String: ")
l=len(x)
c=0
v='aeiouAEIOU'
for i in x:
    if i in v:
        c+=1
print(c)