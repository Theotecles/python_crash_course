from restaurant import Restaurant

restaurant_1 = Restaurant("Jeff Ruby's", 'steakhouse')
print(restaurant_1.name)
print(restaurant_1.cuisine_type)
restaurant_1.describe_restaurant()
restaurant_1.open_or_close()

restaurant_2 = Restaurant('KFC', 'fried chicken')
restaurant_3 = Restaurant('Mizunte', 'mexican')

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

restaurant = Restaurant('Bdubs', 'chicken wings')

restaurant.describe_restaurant()
restaurant.open_or_close()

print(restaurant.number_served)
restaurant.number_served = 2
print(restaurant.number_served)

print(restaurant.number_served)
restaurant.set_number_served(5)
print(restaurant.number_served)

restaurant.increment_number_served(5)
print(restaurant.number_served)