# Constants
HOTEL_PRICE_PER_NIGHT = 110
DAILY_CAR_RENTAL_COST = 50
FLIGHT_PRICES = {
    'Paris': 200,
    'Greece': 600,
    'Egypt': 900,
    'Japan': 1500
}

print("Available destinations: Paris, Greece, Egypt, Japan")

# Ensures user selects available option before proceeding
city_flight = input("Enter the city you will be flying to: ")
destination = ['Paris', 'Greece', 'Egypt', 'Japan']
while city_flight not in destination:
    print('Destination not available. Please choose from: Paris, Greece, Egypt, Japan.')
    city_flight = input("Enter the city you will be flying to: ")

num_nights = int(input("Enter the number of nights you will stay at a hotel: "))
rental_days = int(input("Enter the number of days you will be renting a car: "))

# Function to calculate hotel cost
def hotel_cost(num_nights):
    return num_nights * HOTEL_PRICE_PER_NIGHT

# Function to calculate flight cost
def plane_cost(city_flight):
    return FLIGHT_PRICES.get(city_flight, 0)  # Default to 0 if city not found

# Function to calculate car rental cost
def car_rental(rental_days):
    return rental_days * DAILY_CAR_RENTAL_COST

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
print(f"Total Holiday Cost: £{holiday_cost(num_nights, city_flight, rental_days)}")