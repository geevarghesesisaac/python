#roots of a quadratic equation

import math

a=float(input("enter num a: "))
b=float(input("enter num b: "))
c=float(input("enter num c: "))

dist = b**2 - 4*a*c

if dist>0:
    root1=(-b + math.sqrt(dist)) / (2*a)
    root2=(-b - math.sqrt(dist)) / (2*a)

elif dist==0:
    root1=root2= (-b / (2*a))

else:
    root1= (-b / (2*a))+ (math.sqrt(-dist)/2*a)
    root2= (-b / (2*a))- (math.sqrt(-dist)/2*a)

print(root1, "is root 1")
print(root2, "is root 2")
