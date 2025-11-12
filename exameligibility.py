medical_cause = input("Did you have a medical cause. Kindly enter Y for Yes and N for No")
Attendance = int(input("Kindly enter your attendance"))
if medical_cause  == ("Y"):
    print("You are allowed")
else:
    if Attendance >= 75:
        print("Allowed")
    else:
        print("Not allowed")

