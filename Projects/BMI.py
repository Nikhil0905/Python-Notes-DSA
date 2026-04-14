# To calculate BMI we need weight in Kgs and Height in meters.
w=float(input("Enter weight="))
h=float(input("Enter height="))
BMI=w/h**2
print(BMI)
if BMI<18.5:
    print("UnderWeight")
if BMI>19.0 and BMI<34.5:
    print("Healthy")
if BMI>35:
    print("Overweight")
    