try:
    num1, num2 = eval(input("Enter two numbers separated with a comma: "))
    result = num1/num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is an Error !!!")
except SyntaxError:
    print("No comma separating the numbers. Enter numbers separated by commas, like this: 1, 2")
except:
    print("Wrong Input!!!")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what.")