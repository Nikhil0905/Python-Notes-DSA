for row in range(1,10):
    for col in range(1,10):
        p=row*col
        if p<10:
            print('',p,'',end='')
        else:
            print(p,'',end='')
    print()
    