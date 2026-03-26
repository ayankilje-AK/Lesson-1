class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if (self.a < other.a):
            return ("Object 1 is less than object 2")
        else:
            return ("Object 2 is less than object 1")
    
    def __eq__(self, other):
        if (self.a == other.a):
            return ("Both are equal else not equal")
        else:
            return ("Not Equal")

obj1 = A(2)
obj2 = A(3)
print(obj1.a)
print(obj2.a)
print(obj1<obj2)
obj3 = A(2)
obj4 = A(3)
print(obj3.a)
print(obj4.a) 
print(obj3==obj4)