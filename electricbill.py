unit=float(input("Enter units consumed: "))
if unit>=0 and unit<=150:
    cost=2.75
elif unit>=151 and unit<=250:
    cost=5.25
elif unit>=251 and unit<=500:
    cost=6.30
elif unit>=501 and unit<=800:
    cost=7.10
else:
    cost=7.52

total=unit*cost

print(total, "is your electricity bill")