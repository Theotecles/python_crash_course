# CREATE A LIST OF USERNAMES
usernames = [
    'nuggetry',
    'theotecles',
    'frostypencil',
    'admin',
    'pdiddycombs',
    'shauna0318'
]

# WRITE A FOR LOOP THAT CREATES A GREETING MESSAGE FOR EACH USERNAME
for name in usernames:
    if name == 'admin':
        print(f"Hello {name}, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")

# ADJUST THE STATEMENT ABOVE TO TEST FOR AN EMPTY LIST
usernames = []

if usernames:
    for name in usernames:
        if name == 'admin':
            print(f"Hello {name}, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need to find some users!")

# CREATE A LIST CALLED CURRENT USERS AND NEW USERS MAKING SURE TWO NAMES ARE IN BOTH
current_users = [
    'nuggetry',
    'theotecles',
    'frostypencil',
    'admin',
    'pdiddycombs',
]

current_users_upper = [
    'NUGGETRY',
    'THEOTECLES',
    'FROSTYPENCIL',
    'ADMIN',
    'PDIDDYCOMBS'
]

new_users = [
    'nuggetry',
    'theotecles',
    'shauna0318',
    'sirreginald',
    'regtastic'
]

# CREATE A LOOP TO SEE IF A USERNAME IN THE NEW USERS LIST HAS ALREADY BEEN USED
for name in new_users:
    if name.lower() in current_users and name.upper() in current_users_upper:
        print("Username is already in use. Please try another.")
    else:
        print("Username is available.")
