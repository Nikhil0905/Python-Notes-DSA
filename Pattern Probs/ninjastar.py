
for row in range(10):
    for col in range(15):
        if (row==0 and col==6) or (row==1 and col==5) or ((row ==2) and (col==0 or col==2 or col==1 )) or ((row==3) and col==1) :
            print("*",end=" ")
        elif (row==4 and col==2) or (row==5 and col==1) or (row==6 and col==0) or (row==1 and col==7) :
            print("*",end=" ")
        elif ((row==2) and (col==6 or col==7  or col==8)) or (row==3 and col==10) or (row==4 and col == 9):
            print("*",end=" ")
        elif (row==5 and col==10) or ((row==6) and (col==11)):
            print("*",end=" ")
        elif   (row==5 and col==3 ) or (row==5 and col==7) or (row==4 and col==5):
            print("*",end="")
        
    
        else:
            print(end=" ")
    print()
        