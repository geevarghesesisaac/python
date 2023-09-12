# Write a Python program that uses a `while` loop to count down from limit to 0 and prints each number in the countdown.

limit=int(input("enter limit: "))
count=limit
while count>=0:
    print(count)
    count-=1