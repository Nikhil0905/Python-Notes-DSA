# (1) No. divisible by 3
a=[i for i in range(100) if i%3==0]
print(a)


# (2) Changing to upper case
i=input("Enter str: ").split(",")
l=[i.upper() for i in i]
print(l)

        # or - for horizontal printing (not in list) 

i=input("Enter str: ").split(",")
l=[print(i.upper()) for i in i]


# (3) True and False in bits
bits=[True,False,False,True,False,False,False,False,True,True]
p=[1 if b==True else 0 for b in bits ]
print(p)