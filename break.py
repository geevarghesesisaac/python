llimit=int(input("enter the  lower limit "))
ulimit=int(input("enter the upper limit "))


while llimit<=ulimit:
    if llimit%2!=0:
        print(llimit,"odd")
        llimit+=1
    break
if llimit%2!=1:
    print(llimit,"even")
    llimit+=1
