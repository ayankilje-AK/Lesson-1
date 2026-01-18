def shutdown(command):
    if command == ("Yes"):
        return("Shutdown")
    elif command == ("No"):
        return("Cancel Shutdow")
    else:
        return("Invalid Input")
x = input("Enter your choice: ")
print(shutdown(x))