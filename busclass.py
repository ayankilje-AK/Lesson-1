class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


obj = Bus(" School Volvo", 120, 1000)
print("Vehicle Name: ", obj.name)
print("Vehicle Top Speed: ", obj.max_speed)
print("Vehicle Mileage: ", obj.mileage)
