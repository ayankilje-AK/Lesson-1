print("Welcome to HomeHive")
print("HomeHive lets you buy or rent homes all over the world with just the click of a button.")
name = input("Kindly enter your name: ")
year_of_birth = int(input("Kindly enter the year you were born in: "))
if year_of_birth > 2007:
    print("Sorry, but you must be 18 or above in order to buy or rent a house.")
elif year_of_birth <= 2007 and year_of_birth >= 1965:
    print("You have sucessfully been able to sign in to HomeHive. You now have the ability to buy or rent a house.")
    location = input("Where would you like to look for a house.")