import math
a = int(input("Enter a number: "))
b=a
sum = 0

while a!= 0:
    digit = a % 10
    sum=sum+ math.factorial(digit)
    a=a // 10

if b == sum:
    print("It is a strong number:")
else:
    print("It is a not strong number")