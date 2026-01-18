print("Select your choice of your type of ride")
print("1. Car")
print("2. Bike")
choice = input("Enter your choice for your type of ride")
if choice == "1. Car" or choice == "1 Car" or choice == "1." or choice == "Car" or choice == "1":
    print("You have chosen car")
    print("What type of car would you like to choose?")
    print("1. Sedan")
    print("2. SUV")
    print("3. 4X4 seven seater car")
    choice1 = input("Enter the type of car you would like to ride in")
    if choice1 == choice1 == "1. Sedan" or choice1 == "1 Sedan" or choice1 == "1." or choice1 == "1" or choice1 == "Sedan":
        print("You have chosen the Sedan type of car")
    elif choice1 == "2. SUV" or choice1 == "2 SUV" or choice1 == "SUV" or choice1 == "2" or choice1 == "2.":
        print("You have chosen the SUV type of car")
    elif choice1 == "3. 4X4 seven seater car" or choice1 == "3 4X4 seven seater car" or choice1 == "4X4 seven seater car" or choice1 == "3" or choice1 == "3.":
        print("You have chosen the 4X4 seven seater type of car")
    else:
        print("INVALID CHOICE!")
elif choice == "2. Bike" or choice == "2 Bike" or choice == "Bike" or choice == "2." or choice == "2":
    print("You have chosen Bike")
    print("What type of bike would you like to ride on")
    print("1. Motor Bike")
    print("2. Scooter")
    choice2 = input("Enter your choice of bike that you would likw to ride on")
    if choice2 == "1. Motor Bike" or choice2 == "1 Motor Bike" or choice2 == "Motor Bike" or choice2 == "1." or choice2 =="1":
        print("You have chosen to ride on the Motor Bike kind of bike")
    elif choice2 == "2. Scooter" or choice2 == "2 Scooter" or choice2 == "Scooter" or choice2 == "2." or choice2 == "2":
        print("You have chosen the scooter type of bike")
    else:
        print("INVALID CHOICE!")
else:
    print("INVALID CHOICE ENTERED!") 
