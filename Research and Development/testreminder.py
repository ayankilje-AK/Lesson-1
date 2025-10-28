from datetime import datetime

name=str(input("Enter your name"))
print("Hello" + name + "Welcome to the test reminder app")
print("This is where you can note down your tests and store them in case you forget about it")
print("________________________________________________________________________________________")

print("What is the first test that you will be having")
test1=str(input("Enter the first test that you will be having"))
print("On what date will you be having your test")
date_string = input("Please enter a date in YYYY-MM-DD format: ")
print("The first test that you will be having is" + test1 + "and it will take place on" + date_string)
print("_______________________________________________________________________________________")

print("Now for your second test")
print("What is the second test that you will be having")
test2=str(input("Enter the second test that you will be having"))
print("On what date will your test be taking place on")
date_string2 = input("Kindly enter a date in YYYY-MM-DD format")
print("The second test that you will having is" + test2 + "and it will take place on" + date_string2)
print("_______________________________________________________________________________________")

print("Now for your third test, wait, do you even have a third test")
ans = input("Enter whether you have another test or not. Enter 'Yes' or 'No' ")
if ans == "Yes":
    print("Great \n""What is the third test that you will be having")
    test3=str(input("Enter the third test that you will be having"))
    print("On what date will your test taking place")
    date_string3 = input("Kindly enter a date in YYYY-MM-DD format")
    print("The third test that you will be having is" + test3 + "and it will take place on" + date_string3)
else: 
    print("Ok, come and check back next time if you forget")