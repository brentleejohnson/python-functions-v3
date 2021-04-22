# Functions Handout Task - Sample Solution
def hotel_cost(nights):
    return nights * 140  # in rands


# Plane ride cost
def plane_ride_cost(city):
    if "Cape Town" == city:
        return 2500
    elif "Durban" == city:
        return 2300
    elif "JHB" == city:
        return 2000
    elif "BFN" == city:
        return 1800


# Rental Car Cost
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost = cost - 50
    elif 3 <= days < 7:
        cost = cost - 30
    return cost


def new_sum(*numbers):
    return sum(numbers)


def trip_cost(city, days, spending_money):
    return new_sum(plane_ride_cost(city), hotel_cost(days), rental_car_cost(days), spending_money)


print(trip_cost("Cape Town", 1, 0))
