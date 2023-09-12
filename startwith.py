
a = int(input("Enter a 3 digit number: "))
num = int(input("enter a number "))



while a!= 0:
    temp = a % 10
    a=a//10

if num == temp:
    print("yes:")
else:
    print("no")