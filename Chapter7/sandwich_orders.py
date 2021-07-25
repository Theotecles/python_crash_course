# CREATE A LIST OF SANDWICH ORDERS
sandwich_orders = [
    'pastrami',
    'salami',
    'blt',
    'pastrami',
    'tuna',
    'salami',
    'pastrami',
    'meatball'
]

# CREATE AN EMPTY LIST OF FINISHED SANDWICHES
finished_sandwiches = []

# MAKE MESSAGE THAT SAYS THE RESTAURANT IS OUT OF PASTRAMI
print("Sorry, but we are all out of pastrami!")

# REMOVE PASTRAMIS FROM THE LIST SO THE DONT END UP ON THE FINISHED SANDWICHES
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# CREATE A WHILE LOOP THAT MOVES THE ORDER TO THE FINISHED SANDWICHES
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()

    print(f"Making your {finished_sandwich} sandwich!")
    finished_sandwiches.append(finished_sandwich)

print(finished_sandwiches)