units = int(input("Kindly enter the amount of units you have used"))
if (units < 50):
    amount = units * 2.60
    taxes = 25
elif (units <= 100):
    amount = 130 + ((units - 50)*3.25) 
    taxes = 35
elif (units <= 200):
    amount = 130 + 162.50 + ((units - 100)*5.26)
    taxes = 45
else:
    amount = 130 + 162.50 + 526 + ((units - 200)*8.45)
    taxes = 75
total = amount + taxes
print("The total Electricity Bill cost is = %.2f" %total)