
try:
    number = int(input("Enter a number: "))
    print("The entered number is", number)
except ValueError as ex:
    print("Except: ",ex)