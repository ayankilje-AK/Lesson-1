from abc import ABC, abstractmethod

class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk and run")
class snake(animal):
    def move(self):
        print("I slither and crawl")
class dog(animal):
    def move(self):
        print("I run, I am friendly and I love to play fetch")
class lion(animal):
    def move(self):
        print("I am the king of the animals, the king of the savanah, and we control the circle of life")

obj1 = human()
obj1.move()
obj2 = snake()
obj2.move()
obj3 = dog()
obj3.move()
obj4 = lion()
obj4.move()