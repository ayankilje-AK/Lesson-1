print("Welcome to the AK INDUSTRIES CENTRAL INTELLIGENCE VAULT")
print("You are going to have to sign in to your account. Please proceed to the sign in processes below.")

# Store authorized IDs in a list
authorized_ids = ["AK001", "AK002", "AK003", "ADMIN_99"]

staff_id = input("Enter your STAFF ID: ")
password = input("Please enter your PASSWORD: ")

# Check if the entered ID exists in our list
if staff_id in authorized_ids and password == ("AkAk310114Ak"):
    print("Access Granted.")
else:
    print("Access Denied. Invalid Staff ID.")
    