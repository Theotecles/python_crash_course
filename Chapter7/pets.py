# CREATEA A LIST OF PETS
pets = [
    'dog',
    'cat',
    'dog',
    'goldfish',
    'cat',
    'rabbit',
    'cat'
]
print(pets)

# USE A WHILE LOOP TO REMOVE ALL INSTANCES OF THE VALUE CAT IN THE LIST
while 'cat' in pets:
    pets.remove('cat')

print(pets)