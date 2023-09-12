a=int(input("enter the number: "))
sum=0
pro=1

while (a!=0):
    b=a%10
    sum=sum+b
    pro=pro*b
    a=a//10

if(sum==pro):
    print("it is a spy number")
else:
    print("it is a not spy number")