try:
    age = int(input("Enter your age: "))
    if age <= 0:
        print("Invalid age. Age cannot be 0 or less.")
    else:
        print("Age is valid")
        if age %2 == 0:
            print("You age is an even number.")
        else:
            print("Your age is an odd number.")
except ValueError:
    print("Please enter the valid number.")
    
