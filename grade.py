#grade of student

mark=float(input("enter your mark in outoff 50 : "))
percentage=(mark/50)*100

if percentage>=90 and percentage<=100:
    print("Your grade is A")
elif percentage>=80 and percentage <=89:
    print("Your grade is B")
elif percentage>=70 and percentage <=79:
    print("Your grade is C")
elif percentage>=60 and percentage <=69:
    print("Your grade is D")
elif percentage>=50 and percentage <=59:
    print("Your grade is E")
else:
    print("You failed!")
    