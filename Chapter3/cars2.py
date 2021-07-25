# CREATE A LIST OF CARS

cars = ['bmw',
		'audi',
		'toyota',
		'subaru']

# ARRANGE CARS ALPHABETICALLY WITH SORT METHOD

cars.sort()
print(cars)

# ARRANGE CARS IN REVERSE ALPHABETICAL ORDER

cars.sort(reverse=True)
print(cars)

# ARRANGE THE LIST TEMPORARILY WITH THE SORTED FUNCTION

cars = ['bmw',
		'audi',
		'toyota',
		'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again")
print(cars)

# REVERSE THE ORDER OF THE LIST

cars = ['bmw',
		'audi',
		'toyota',
		'subaru']

print(cars)

cars.reverse()
print(cars)

# CHECK THE LENGTH OF A LIST

cars = ['bmw',
		'audi',
		'toyota',
		'subaru']

print(len(cars))