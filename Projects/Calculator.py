k = float(input("Enter a no.="))
l = float(input("\nEnter another no.="))
def add():
    print(k + l)
def multiply():
    print(k * l)
def division():
    print(k / l)
def remainder():
    print(k % l)
def subtract():
    print(k - l)
def power():
    print(k ** l)
print("\n+add")
print("\n*multiply")
print("\n/division")
print("\n%remainder")
print("\n-subtraction")
print("\n**power")
print("\n0exit")
c = input("Enter Option")
if c == '+':
    add()
elif c == '*':
    multiply()
elif c == '/':
    division()
elif c == '%':
    remainder()
elif c == '-':
    subtract()
elif c =='**':
    power()

print()
