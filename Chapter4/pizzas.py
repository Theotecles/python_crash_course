# CREATE A LIST OF MY FAVORITYE PIZZAS

pizzas = [
    'pepperoni',
    'sausage',
    'spinach',
    'margherita',
    'veggie']

# CREATE A FOR LOOP THAT PRINTS THE NAME OF EACH PIZZA

for pizza in pizzas:
	print(pizza)

# CREATE A FOR LOOP THAT PRINTS A SHORT SENTENCE WITH THE NAME OF EACH PIZZA

for pizza in pizzas:
	print(f"I like {pizza} pizza!")

# CREATE A FOR LOOP THAT PRINTS THE SAME SENTENCES ABOVE AND ADDS ANOTHER SENTENCE AT THE END

for pizza in pizzas:
	print(f"I like {pizza} pizza!")

print("\nPizza rules so hard bro.")

# PRINT THE FIRST THREE ITEMS IN THE LIST

print('The first three items in the list are:')
print(pizzas[0:3])

# PRINT THE MIDDLE THREE ITEMS IN THE LIST

print('The middle three items in the list are:')
print(pizzas[1:4])

# PRINT THE LAST THREE ITEMS IN THE LIST

print('The last three items in the list are')
print(pizzas[-3:])

# COPY THE LIST

friend_pizzas = pizzas[:]

# ADD A NEW PIZZA TO THE ORIGINAL LIST AND FRIENDS LIST

pizzas.append('briar hill')
friend_pizzas.append('bbq chicken')

# PRINT BOTH LISTS

print('My favorite pizzas are:')
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
