a=int(input("enter the number "))
sum=0

while a!= 0:
    temp = a % 10

    if temp%2==0:
        sum=sum+temp
    a=a//10
    

print("sum =", sum )
