#define a function called hotel cost
def hotel_cost(nights):
    return 140*nights

#define a function called plane ride cost
def plane_ride_cost(city):
    if city == ("Charlotte"):
        return 183
    elif city == ("Tampa"):
        return 220
    elif city == ("Pittsburgh"):
        return 222
    elif city == ("Los Angeles"):
        return 475
    
#define a function called rental car cost
def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days
    
#define a function called trip cost
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of car rental: ", rental_car_cost(7))
print("Plane ride cost: ", plane_ride_cost("Los Angeles"))
print("The hotel cost: ", hotel_cost(8))
print("The trip cost: ", trip_cost("Los Angeles", 12, 12500))
print("Trip cost: ", trip_cost("Tampa", 12, 8000))