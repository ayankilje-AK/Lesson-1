class BMW:
    def fuel_type(self):
        return "Diesel or Petrol"

    def max_speed(self):
        return "250 km/h"

class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"

# Polymorphism in action using a common interface
def car_details(car):
    print(f"Fuel: {car.fuel_type()}")
    print(f"Max Speed: {car.max_speed()}")

# Create objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Accessing methods via the same function
print("BMW Details:")
car_details(bmw_car)

print("\nFerrari Details:")
car_details(ferrari_car)
