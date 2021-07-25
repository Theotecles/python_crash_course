# CREATE A LIST OF FOODS

my_foods = [
    'pizza',
    'falafel',
    'carrot cake']

# COPY THE LIST

friends_foods = my_foods[:]

# PRINT BOTH LISTS

print("My favorite foods are:")

for food in my_foods:
	print(food)

print("\nMy friends' favorite foods are:")

for food in friends_foods:
	print(food)

# ADD AN ELEMENT TO BOTH ENDS

my_foods.append('cannoli')
friends_foods.append('ice cream')

# REPRINT THE LISTS

print("My favorite foods are:")

for food in my_foods:
	print(food)

print("\nMy friends' favorite foods are:")

for food in friends_foods:
	print(food)

# TRY TO COPY A LIST WITHOUT USING A SLICE
# THIS WONT WORK

friends_foods = my_foods

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friends' favorite foods are:")
print(friends_foods)