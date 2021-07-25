# CREATE A FUNCTION CALLED GREET_USERS
def greet_users(names):
    """PRINT A SIMPLE GREETING TO EACH USER IN THE LIST."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = [
    'hannah',
    'ty',
    'margot'
]
greet_users(usernames)