n = int(input("Enter: "))
list = []
for i in range(1, n):
    if 2**i == n:
        list.append(1)
    else:
        continue
if len(list) > 0:
    print("YES")
else:
    print("NO")