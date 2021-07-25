#CREATE A DICTIONARY OF FAVORITE NUMBERS
favorite_numbers = {
    'brian': 13,
    'shauna': 7,
    'ben': 21,
    'evan': 28,
    'peter': 12,
}

# PRINT EACH PERSON'S NAME AND THE NUMBER
for i in favorite_numbers:
    print(f"{i.title()}'s favorite number is {favorite_numbers[i]}")

# CHANGE IT SO EACH PERSON CAN HAVE MORE THAN ONE FAVORITE NUMBER
favorite_numbers = {
    'brian': [13, 7, 25, 66],
    'shauna': [7, 12, 21],
    'ben': [21, 22],
    'evan': [28, 8, 16, 24, 32, 45, 69],
    'peter': [12, 17]
}

# LOOP THROUGH SO EACH PERSON HAS THEIR FAVORITE NUMBERS LISTED UNDERNEATH THEIR NAME
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")