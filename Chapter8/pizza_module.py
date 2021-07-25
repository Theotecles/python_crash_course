def make_pizza(size, *toppings):
    """SUMMARIZE THE PIZZA WE ARE ABOUT TO MAKE"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")