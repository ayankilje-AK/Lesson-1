from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self, x):
        print(x)
    @abstractmethod
    def task(self):
        print("We are inside Abs class task")

class test_class(Absclass):
    def task(self):
        print(" We are inside test_class task")

obj1 = test_class()
obj1.task()
obj1.print(123)