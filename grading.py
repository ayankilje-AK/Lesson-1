mark1 = int(input("Enter the score for your first subject"))
mark2 = int(input("Enter the score for your second subject"))
mark3 = int(input("Enter the score for your third subject"))
mark4 = int(input("Enter the score for your fourth subject"))
mark5 = int(input("Enter the score for your fifth subject"))

sum = mark1 + mark2 + mark3 + mark4 + mark5
average = sum/5

if average >= 91 and average <= 100:
    print("Your grade is A1")
elif average >= 81 and average < 91:
    print("Your grade is A2")
elif average >= 71 and average < 81:
    print("Your rade is B1")
elif average >= 61 and average < 71:
    print("Your grade is B2")
elif average >= 51 and average < 61:
    print("Your grade is C1")
elif average >= 41 and average < 51:
    print("Your grade is C2")
elif average >= 33 and average < 41:
    print("Your grade is D")
elif average >= 21 and average < 33:
    print("Your grade is E1")
elif average >= 0 and average < 21:
    print("Your grade is E2")
else:
    print("INVALID INPUT!")
