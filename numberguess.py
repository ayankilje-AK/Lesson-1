import random
import time

number = random.randint(1, 100)

def intro():
    print("May I ask for your name")
    global Name
    name = input("Kindly enter your name: ")
    print("Hi"+ name + "We are going to play a game. You will have to guess a number from 1 to 100")
    if number %2 == 0:
        x = 'Even'
    else:
        x = 'Odd'
    print("This is an {} number".format(x))
    time.sleep(.5)
    print("Go ahead and guess")
    
def pick():
    guesses_taken = 0
    while guesses_taken < 6:
        time.sleep(.25)
        enter = input("Enter your guess: ")

        try:
            guess = int(enter)
            if guess <= 100 and guess >= 1:
                guesses_taken += 1
                if guesses_taken < 6:
                    if guess < number:
                        print("The number that you have entered as your guess is too low.")
                    if guess > number:
                        print("The number that you have entered as your guess is too high.")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again")
                    if guess == number:
                        break
            if guess > 100 or guess < 1:
                print("That number is not in the range.")
                time.sleep(.25)
                print("Please enter a number between 1 and 100")
        
        except:
            print("I don't think that" + enter + "is a number, Sorry.")
    if guess == number:
        guesses_taken = str(guesses_taken)
        print(f"Good Job, you guessed the right number. {number}")
    if guess != number:
        print("The number I was thinking of was " + str(number))

play_again = "Yes"
while play_again == "Yes" or play_again == "Y" or play_again == "YES" or play_again == "y":
    intro()
    pick()
    print("Do you want to play again?")
    play_again = input("Enter whether you would like to play again. Y/ N")
    