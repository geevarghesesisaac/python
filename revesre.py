num=int(input("enter a number: "))
revesred_num=0

while num>0:
    last_digit=num%10
    num=num//10
    revesred_num=revesred_num*10 + last_digit

print("revsrded number", revesred_num )
