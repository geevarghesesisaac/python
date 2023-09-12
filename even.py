#Create a Python program that uses a `while` loop to print all the even numbers from 1 to 20

limit=int(input("enter the limit "))
count=0
while count<=limit:
    if(count%2==0):
        print(count)
    count+=1