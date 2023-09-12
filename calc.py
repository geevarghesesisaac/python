num1=int(input("enter numb 1 "))
num2=int(input("enter numb 2 "))

print("insert 1 for sum \n insert 2 for substraction \n insert 3 for multiplication \n insert 4 for division  ")

task=int(input("input the task"))

if task==1:
    result=num1+num2
    print(result)
elif task==2:
    result=num1-num2
    print(result)
elif task==3:
    result=num1*num2
    print(result)
elif task==4:
    result=num1/num2
    print(result)
else:
    print("invalid")