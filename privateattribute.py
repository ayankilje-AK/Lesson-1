class myclass:
    
    __privatevar = 27; 
    def __privatemethod(self):
        print("I am inside the class")
    def hello(self):
        print(myclass.__privatevar)

obj1 = myclass()
obj1.hello()
obj1.__privatemethod