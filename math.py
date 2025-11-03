print("Welcome to AK Math Solver")
print("This is where you can solve different kinds of Mathematics problems")
print("To begin, kindly enter your name")
name = str(input("Enter your name: "))
print("Welcome to AK Math Solver", name)
print("What kind of problem would you like to solve today", name)
print("1. Addition, Subtraction, Multiplication, and Division of whole numbers")
print("2. Finding the Square Root of a number")
print("3. Finding the average of numbers")
print("4. Converting decimals to fractions")
choice = input("Enter your choice. 1/2/3/4:  ")
if choice == ("1"):
    print("Welcome to the Addition, Subtraction, Multiplication and Division of whole numbers Calculator")
    print("First, please enter the two numbers that you would like to operate on")
    num1 = int(input("Enter your first operating number"))
    num2 = int(input("Enter your second operating number"))
    print("The two numbers that you will be operating on today are", num1,"and", num2)
    print("What would you like to do")
    print("a. Add")
    print("b. Subtract")
    print("c. Multiply")
    print("d. Divide")
    choice1 = input("What would you like to do. a/b/c/d")
    if choice1 == ("a"):
        result = (num1 + num2)
        print("The answer to", num1, "+", num2,"is", result)
    elif choice1 == ("b"):
        result1 = (num1 - num2)
        print("The answer to", num1,"-", num2,"is", result1)
    elif choice1 == ("c"):
        result2 = (num1 * num2)
        print("The answer to", num1,"x", num2,"is",result2)    
    elif choice1 == ("d"):
        result3 = (num1 / num2)
        print("The answer to", num1,"÷", num2,"is", result3)
elif choice == ("2"):
    print("Welcome to the Square Root Finder")
    print("This is where you can find the square root of any number")


