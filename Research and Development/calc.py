print("Calc-X")
print("Welcome to Calc-X")
print("Calc-X is a platform in which you can either add, subtract, divide or multiply any two whole numbrs")
print("Lets start of with your details")
name=str(input("Enter your name here:  "))
print("Hello", name)
print("___________________________________________________________________________________")
print("Now onto the numbers")
print("Enter your first operating number")
num1=int(input("Enter the first number that you would like to operate:  "))
print("Now for your second operating number")
num2=int(input("Enter your second operating number"))
print("___________________________________________________________________________________")
print("What operator would you like to use to operate your two numbers")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter your choice. 1/2/3/4")
if choice == ("1"):
    result = (num1+num2)
    print("The answer to", num1, "+", num2, "is", result)
elif choice == ("2"):
    result2 = (num1-num2)
    print("The answer to", num1, "-", num2, "is", result2)
elif choice == ("3"):
    result3 = (num1*num2)
    print("The answer to", num1, "x", num2,"is", result3)
elif choice == ("4"):
    result4 = (num1/num2)
    print("The answer to", num1, "÷", num2, "is", result4)


print("Now would you like to get the answer for all, addition, subtraction, multiplication, and division")
print("Yes")
print("No")
choice2 = input("Enter your choice exactly as given. Yes/No")
if choice2 == ("Yes"):
    print("Addition",result)
    print("Subtraction",result2)
    print("Multiplication",result3)
    print("Division", result4)
else:
    print("Thank you for using Calc-X")
    print("Hope you use Calc-X again")


    
    



