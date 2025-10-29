num=int(input("Enter the number less than 15 that you would to compare to 15:  "))

if num > 15:
    print(num,"is greater than 15")
else:
    print(num,"is not greater than 15")
    required_15 = (15 - num)
    print("You would need to add", required_15,"to be able to get 15 exactly")