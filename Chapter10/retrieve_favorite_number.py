import json
filename = 'favorite_number.json'

with open(filename) as f:
    favorite_number = json.load(f)

print(f"I know your favorite number is {favorite_number}")