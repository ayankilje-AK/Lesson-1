import random

print("Welcome to the Nuber Guessing Game")
print("I'm thinking of a number between 1 and 100, can you find the number, if you find it within 7 tries, you win, or else you must take on a dare")
name = str(input("Kindly enter your name to proceed"))
print("Welcome to the Number Guessing Game", name)


secret_number = random.randint(1,100)
attempts = 0
guessed_correctly = False

while not guessed_correctly:
    try:
        user_guess = int(input("Enter your guess"))
        attempts += 1
        if user_guess < 1 or user_guess > 100:
            print("Please enter a guess between 1 and 100")
        elif user_guess < secret_number:
            print("Too Low! Try a higher number")
        elif user_guess > secret_number:
            print("Too High! Try a lower number")
        else:
            print("Congratulations! You have guessed the number", secret_number)
            guessed_correctly = True
    except ValueError:
        print("Invalid Input. Please enter a whole number")

