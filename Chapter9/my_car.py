from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# MODIFY THE ATTRIBUTES VALUE DIRECTLY
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# MODIFY THE ATTRIBUTES VALUE USING A METHOD
# ADDED IN THE UPDATE ODOMETER METHOD ABOVE
my_new_car.update_odometer(32)
my_new_car.read_odometer()

# DEFINE A USED CAR
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()