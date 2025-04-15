print("Available destinations: Paris, Greece, Egypt, Japan")

# Ensures user selects available option before proceeding
city_flight = input("Enter the city you will be flying to: ")
destination = ['Paris', 'Greece', 'Egypt', 'Japan']
while city_flight not in destination:
    print('destination not available. Please choose from: Paris, Greece, Egypt, Japan.')
    city_flight = input("Enter the city you will be flying to: ")

num_nights = int(input("Enter the number of nights you will stay at a hotel: "))
rental_days = int(input("Enter the number of days you will be renting a car: "))

# Function to calculate hotel cost based on the number of nights
def hotel_cost(num_nights):
    hotel_price = 110
    return num_nights * hotel_price

# Function to calculate flight cost based on selected destination
def plane_cost(city_flight):
    if city_flight == 'Paris':
        paris_flight = 200
        return paris_flight
    elif city_flight == 'Greece':
        greece_flight = 600
        return greece_flight
    elif city_flight == 'Egypt':
        egypt_flight = 900
        return egypt_flight
    elif city_flight == 'Japan':
        japan_flight = 1500
        return japan_flight
    else:
        return "Invalid city"

# Function to calculate car rental cost
def car_rental(rental_days):
    daily_rental_cost = 50
    total_rental_cost = rental_days * daily_rental_cost
    return total_rental_cost

# Function to calculate total holiday cost
def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel = hotel_cost(num_nights)
    total_plane = plane_cost(city_flight)
    total_car = car_rental(rental_days)
    total_cost = total_hotel + total_plane + total_car
    return total_cost

# Display the results
print("\n--- Holiday Cost Summary ---")
print(f"Destination: {city_flight}")
print(f"Hotel Cost: £{hotel_cost(num_nights)}")
print(f"Flight Cost: £{plane_cost(city_flight)}")
print(f"Car Rental Cost: £{car_rental(rental_days)}")
print(f"Total Holiday Cost: £{holiday_cost( num_nights, city_flight, rental_days)}")
