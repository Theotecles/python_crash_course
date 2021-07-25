# CREATE A FUNCTION CALLED MAKE TSHIRT
def make_tshirt(size, message):
    """THIS FUNCTION WILL PRINT THE SIZE AND MESSAGE OF THE TSHIRT THAT IS BEING MADE"""
    print(f"The Tshirt size you selected is {size} and the message is '{message}'.")

make_tshirt('Large', 'Reggie is one bomb dog')

# MODIFY THE FUNCTION SO IT HAS DEFAULT ARGUMENTS
def make_tshirt(size='Large', message='I love Python.'):
    """THIS FUNCTION WILL PRINT THE SIZE AND MESSAGE OF THE TSHIRT THAT IS BEING MADE"""
    print(f"The Tshirt size you selected is {size} and the message is '{message}'.")

make_tshirt()
make_tshirt('medium')
make_tshirt(message='Reggie is a bomb dog')