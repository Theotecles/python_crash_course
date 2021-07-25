# STORE INFORMATION ABOUT A PIZZA BEING ORDERED
pizza = {
    'crust': 'thick',
    'toppings': [
        'mushrooms',
        'extra cheese'
    ]
}

# SUMMARIZE THE ORDER
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")