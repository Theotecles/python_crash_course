import json

try:
    filename = 'favorite_number.json'
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    print("We couldn't find your number please tell us what it is.")
    favorite_number = int(input("What is your favorite number? "))
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    print("We stored your favorite number and know it for next time")
else:
    print(f"I know your favorite number! It's {favorite_number}")