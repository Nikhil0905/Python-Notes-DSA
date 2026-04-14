# s=open(r"C:\Users\nikhi\OneDrive\Documents\Notepad File Handling\GD Rules.txt")
# rl=s.readlines()
# for i in rl:
# print(i[::-1].strip())           ## Strip is used in loops only to remove extra \n 
# s.read()
# n=int(input("Read From: "))
# s.seek(n)
# print(s.read())
# s.close()


               ## To read The words 
s=open(r"C:\Users\nikhi\OneDrive\Documents\Notepad File Handling\GD Rules.txt")
read=s.read()
print(read.strip())
print(read)
l=[]
for i in read:
    if i!=" ":
        print(i,end="")
