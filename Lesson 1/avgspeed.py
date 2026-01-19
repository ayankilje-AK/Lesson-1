speed1 = int(input("Enter the the speed of the first bicycle"))
speed2 = int(input("Enter the speed of the second bicycle"))
speed3 = int(input("Enter the speed of the third bicycle"))

average = (speed1 + speed2 + speed3)/3
print("The average of the three speeds is", average)

if average > speed1 and average > speed2 and average > speed3:
    print("%d is higher than %d, %d, %d" %(average, speed1, speed2, speed3))
elif average > speed1 and average > speed2:
    print("%d is higher than %d, %d" %(average, speed1, speed2))
elif average > speed1 and average > speed3:
    print("%d is greater than %d, %d" %(average, speed1, speed3))
elif average > speed2 and average > speed3:
    print("%d is greater than %d, %d" %(average, speed2, speed3))
elif average > speed1:
    print("%d is greater than %d" %( average, speed1))
elif average > speed2:
    print("%d is greater than %d" %( average, speed2))
elif average > speed3:
    print("%d is greater than %d" %( average, speed3))
else:
    print("INVALID INPUT!")