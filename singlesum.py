a = int(input("Enter a number: "))
sum = 0

while a > 0:
    digit = a % 10
    sum+= digit
    a //= 10

a = sum

print("The sum of digits:", a)
