import json

def get_stored_username():
    """GET STORED USERNAME IF AVAILABLE"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """PROMPT FOR A NEW USERNAME"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """GREET THE USER BY NAME"""
    username = get_stored_username()
    answer = input(f"Are you {username}? (Enter 'Yes' or 'No') ")
    if answer.lower() == 'no':
        username = get_new_username()
    else:
        if username:
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We;ll remember you when you come back, {username}!")

greet_user()