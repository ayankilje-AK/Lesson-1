import random
playing = True
number = str(random.randint(0,9))
print("I have generated a number from 0 to 9. Guess the number to win the game")
while playing:
    guess = input("Enter your guess in the form of an integer: ")
    if number == guess:
        print("You have won the game")
        print(f"The number was {number}")
        break
    else:
        print("Your guess isn't quite right, please try again. \n")