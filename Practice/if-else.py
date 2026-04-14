value=int(input("Enter Value: "))
for VAL in range(0,value):
   if VAL%4==0:
       print(VAL*4)
   elif VAL%5==0:
       print(VAL+3)
   else:
       print(VAL+10)
       