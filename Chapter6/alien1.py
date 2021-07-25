# THERE WILL BE EXAMPLES OF NESTING BELOW
# CREATE MULTIPLE DICTIONARIES FOR EACH ALIEN
alien_0 = {
    'color': 'green',
    'points': '5'
}

alien_1 = {
    'color': 'yellow',
    'points': '10'
}

alien_2 = {
    'color': 'red',
    'points': '15'
}

# CREATE A LIST THAT CONTAINS THE DICTIONARIES
aliens = [
    alien_0,
    alien_1,
    alien_2
]

# CREATE A FOR LOOP THAT PRINTS EACH DICTIONARY
for alien in aliens:
    print(alien)

# CREATE A LIST OF ALIENS BUT MORE EFFICIENTLY
# MAKE AN EMPTY LIST FOR STORING
aliens = []

# MAKE 30 GREEN ALIENS
for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# SHOW THE FIRST 5 ALIENS
for alien in aliens[:5]:
    print(alien)
print("...")