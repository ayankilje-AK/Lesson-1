print("Welcome to AK mathBOT - your utimate Math Solver")
print("To begin, kindly enter your name")
name = input("Kindly enter your name: ")
print("Welcome to AK mathBOT", name)
print("What kind of mathematics problem will you be solving today")
print("1. Arithmetical Calculations")
print("2. Square Root Finder")
print("3. Conversion of Fractions to Decimals")
choice = input("Kindly enter your choice. 1/2/3/ : ")
if choice == ("1"):
    print("You have chosen to perform Arithmetical Calculations \n Addition, Subtraction, Multiplication and Division of Numbers")
    print("How many numbers would you be calculating")
    print("2")
    print("3")
    print("4")
    num_of_numbers = int(input("Kindly enter the amount of numbers you will be calculating on. 2/3/4: "))
    if num_of_numbers == ("2"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("What operator would you like to use")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        operator = input("Enter your operator. 1/2/3/4")
        if operator == ("1"):
            result = (num1+num2)
            print(f"The answer to {num1} + {num2} is {result}")
        elif operator == ("2"):
            result = (num1 - num2)
            print(f"The answer to {num1} - {num2} is {result}")
        elif operator == ("3"):
            result = (num1*num2)
            print(f"The answer to {num1} X {num2} is {result}")
        else:
            result = (num1 / num2)
            print(f"The answer to {num1} ÷ {num2} is {result}")
    elif num_of_numbers == ("3"):
        num1 = float(input("Kindly enter the first number"))
        num2 = float(input("Kindly enter the second number"))
        num3 = float(input("Kindly enter the third number"))
        print("What operator would you like to use")
        print("1. Additon") 
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        operator = input("Enter your operator choice. 1/2/3/4")
        if operator == ("1"):
            result = (num1 + num2 + num3)
            print(f"The answer to {num1} + {num2} + {num3} is {result}")
        elif operator == ("2"):
            result = (num1 - num2 - num3)
            print(f"The answer to {num1} - {num2} - {num3} is {result}")
        elif operator == ("3"):
            result = (num1*num2*num3)
            print(f"The answer to {num1} X {num2} X {num3} is {result}")
        else:
            result = (num1/num2/num3)
            print(f"The answer to {num1} ÷ {num2} ÷ {num3} is {result}")
    elif num_of_numbers == ("4"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        num4 = float(input("Enter the fourth number: "))
        print("what operator will you be using")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        operator = input("Enter your operator choice. 1/2/3/4")
        if operator == ("1"):
            result = (num1+num2+num3+num4)
            print(f"The answer to {num1} + {num2} + {num3} + {num4} is {result}")
        elif operator == ("2"):
            result = (num1 - num2 - num3 - num4)
            print(f"The answer to {num1} - {num2} - {num3} - {num4} is {result}")
        elif operator == ("3"):
            result = (num1*num2*num3*num4)
            print(f"The answer to {num1} * {num2} * {num3} * {num4}")
        elif operator == ("4"):
            result = (num1/num2/num3/num4)
            print(f"The answer to {num1} ÷ {num2} ÷ {num3} ÷ {num4} is {result}")

elif choice == ("2"):
    import math
    print("You have chosen the square root finder")
    
    num = int(input("Enter the number you would like to find the square root of: "))
    square_root = math.sqrt(num)
    print("The square root of", num, "is", square_root)

elif choice == ("3"):
    print("You have chosen the Fraction to percentage converter")
    print("Over here, You could be able to convert fractions into percentages")
    numerator = float(input("Enter the fraction numerator: "))
    denominator = float(input("Enter the fraction denominator: "))
    percentage = (numerator/denominator)*100
    print(f"The percentage is {percentage}%")


