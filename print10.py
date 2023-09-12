llimit=int(input("enter the  lower limit "))
ulimit=int(input("enter the upper limit "))


while llimit<=ulimit:
    if llimit%2!=0:
        print(llimit,"odd")
    else:
        print(llimit,"even")
    llimit+=1
