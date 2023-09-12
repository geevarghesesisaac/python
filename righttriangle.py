#if the given measurements form a right-angled triangle

#Obtain the measurements of the three sides of the triangle (a, b, and c)
sidea=float(input("enter lenght of side a: "))
sideb=float(input("enter lenght of side b: "))
sidec=float(input("enter lenght of side c: "))

#Calculate the squares of the lengths of the three sides
squarea=sidea**2
squareb=sideb**2
squarec=sidec**2

#Check if the Pythagorean theorem holds true

if(squarea+squareb==squarec):
    print("it is right-angled trangle")
elif(squarec+squarea==squareb):
    print("it is right-angled trangle")
elif(squareb+squarec==squarea):
    print("it is right-angled trangle")
else:
    print("it is not right-angled triangle")
