class Vehicle:

    def __init__(self, capacity):
        self.capacity = capacity

class Bus(Vehicle):

    def total_fare(self):
        fare_per_person = 50
        total = self.capacity * fare_per_person
        return total

obj =  Bus(50)
print(obj.capacity)
print(obj.total_fare())