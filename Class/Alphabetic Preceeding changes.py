"""Write a program where you use class to implement the following :
---> take input from user as string which consists of of upper & lower case character Now change the character based in alphabetical order.
---> if the preceeding character of current character lies in the alphabetical order keep the current in lowercase if the preceeding character lies
 behind in alphabetical order make the current uppercase, if both are equal don't change case ,After space is encountered keep the next character case.
 Ex.- CoOL dog ----> COOl dOg
"""


a=input("string: ")
l=len(a)
b=list(a)
for i in b:
    for j in range(l):
        if ord(i)<ord(i+1) or ord(i)==ord(i+1):
            i=i.upper()
        elif ord(i)>ord(i+1):
            i=i.lower()
        elif i==" ":
            pass
        else:
            continue
print(i,end="")

        
