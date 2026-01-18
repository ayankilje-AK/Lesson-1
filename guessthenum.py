import random

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100, can you find the number in 7 tries")
name = str(input("Enter your name to play the game"))
print("You are participating in the Number Guessing Game", name)

secret_number = random.randint(1,100)
attempts = 0
guessed_correctly = False

while not guessed_correctly:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        if user_guess < 1 or user_guess > 100:
            print("Please enter a guess between 1 and 100")
        elif user_guess < secret_number:
            print("Too Low! Try a higher number")
        elif user_guess > secret_number:
            print("Too high! Try a lower number")
        else:
            print("Congratulations, you have guessed the secret number which was", secret_number, "in", attempts, "attempts")
            guessed_correctly = True
    except ValueError:
        print("INVALID INPUT! Please enter a whole number")