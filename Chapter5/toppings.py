# CREATE A VALUE CALLED REQUESTED TOPPING
requested_topping = 'mushrooms'

# CREATE AN IF STATEMENT TO PRINT SOMETHING IF IT ISNT EQUAL TO ANCHOVIES
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# CREATE A NEW LIST OF REQUESTED TOPPINGS
requested_toppings = [
    'mushrooms',
    'extra cheese'
]

# WRITE AN IF STATEMENT THAT CREATES THE PIZZA
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")

# CREATE ANOTHER LIST OF REQUESTED TOPPINGS
requested_toppings = [
    'mushrooms',
    'green peppers',
    'extra cheese'
]

# CREATE A FOR LOOP
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# CREATE AN IF STATEMENT WITHIN THE FOR LOOP TO ACCOUNT FOR NO GREEN PEPPERS
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# CREATE AN EMPTY LIST
requested_toppings = []

# WRITE AN IF STATEMENT AND A FOR LOOP
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinishing making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# CREATE A LIST OF AVAILABLE TOPPINGS
available_toppings = [
    'mushrooms',
    'olives',
    'green peppers',
    'pepperoni',
    'pineapple',
    'extra cheese'
]

requested_toppings = [
    'mushrooms',
    'french fries',
    'extra cheese'
]

# CREATE A FOR LOOP AND AN IF STATEMENT THAT OMITS TOPPINGS NOT AVAILABLE
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we dont have {requested_topping}.")

print("\nFinished making your pizza!")