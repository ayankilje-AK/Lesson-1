class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius * self.radius
    def parameter(self):
        return 2*3.14*self.radius

obj1 = Circle(145)
print(obj1.radius)
print(obj1.area())
print(obj1.parameter())


        