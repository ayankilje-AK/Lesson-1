import random

class fruitquiz:
    def __init__(self):
        self.fruits = {'apple': 'red', 'orange': 'orange', 'watermelon':'green', 'banana':'yellow'}
    def quiz(self):
        while True:
            fruit, colour = random.choice(list(self.fruits.items()))
            print("What is the colour of {}?".format(fruit))
            user_answer = input("Ener your answer: ")
            if (user_answer.lower()==colour):
                print("Correct Answer")
            else:
                print("Wrong answer")
            option = int(input("Enter 0 if you want to play again, otherwise enter 1"))
            if (option):
                break
print("Welcome to fruitquiz")
obj1 = fruitquiz()
obj1.quiz()

