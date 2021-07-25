# CREATE A FUNCTION THAT HAS AN ARBITRARY NUMBER OF ARGUMENTS
def make_pizza(*toppings):
    """ PRINT THE LIST OF TOPPINGS THAT HAVE BEEN REQUESTED."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# MODIFY THE FUNCTION SO IT DESCRIBES THE PIZZA THAT IS BEING ORDERED
def make_pizza(*toppings):
    """SUMMARIZE THE PIZZA WE ARE ABOUT TO MAKE"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# MODIFY THE FUNTION SO IT TAKES INTO ACCOUNT BOTH POSITIONAL AND ARBITRARY ARGUMENTS
def make_pizza(size, *toppings):
    """SUMMARIZE THE PIZZA WE ARE ABOUT TO MAKE"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')