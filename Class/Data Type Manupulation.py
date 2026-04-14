l=[11,21,22,26,24,26,12,13,14,15,16,17]
s1={21,22,23,24,25,26}
tup=(31,32,33,34,35,36)
d={1:'a',2:'b',3:'c',4:'d',5:'e'}
l2=list(s1)
print(l2)
s2=set(l)
print(s2)
print("Repeated int are:",len(l)-len(l2))
l[3]='Hello World'
print(l)
print(l.pop(1))
l.insert(3,"Mango")
print(l)
for i in range(len(l)):
    if i%2==0:
        a=input("New Element:")
        l[i]=a
    else:
        continue
print(l)
print(l[::-1])
print(l[-5::-1])
dk=d.keys()
print(dk)
print(type(dk))
l3=list(dk)
print(l3)
dv=d.values()
print(dv)
print(d[2])
l5=list(d.keys())
l5.append(6)
l6=list(d.values())
l6.append("g")
print(dict(zip(l5,l6)))
d.update({7:'j'})
print(d)

