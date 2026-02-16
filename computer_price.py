class computer:

    def __init__(self):
        self.__maxprice =  900
    def sell(self):
        print("Selling price {}".format(self.__maxprice))
    def setmaxprice(self, price):
        self.__maxprice = price

obj1 = computer()
obj1.sell()
obj1.__maxprice = 1000
obj1.sell()
obj1.setmaxprice(1000)
obj1.sell()