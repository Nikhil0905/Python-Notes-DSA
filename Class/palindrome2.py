
num = input("Enter: ")
if num == num[::-1]:
    print(f"The number {num} is a Palindrome.")
else:
    print(f"The number {num} is NOT Palindrome.")
    temp = num
    count = 0
    while True:
        print(f"{temp} + {temp[::-1]}")
        temp = str(int(temp) + int(temp[::-1]))
        count += 1
        print(f"New number: {temp}")
        if temp == temp[::-1]:
            print(f"The number {temp} is a Palindrome.")
            print(f"Found palindrome after {count} iterations.")
            break
        else:
            print(f"The number {temp} is NOT Palindrome.")
