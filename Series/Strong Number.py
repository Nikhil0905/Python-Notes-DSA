# A number who's digit's factorial's sum is equal to it's original number
n = int(input("Enter a number: "))
e = n
c = 1
s = 0

while n > 0:
    r = n % 10
    f = 1
    for i in range(1, r + 1):
        f *= i
    s += f
    n = n // 10

if s == e:
    print("Strong number")
else:
    print("Not a Strong Number")
            