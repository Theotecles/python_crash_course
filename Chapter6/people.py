# CREATE A LIST WITH A DICTIONARY OF PROPLE
people = [
    {
        'first_name': 'shauna',
        'last_name': 'combs',
        'age': 26,
        'city': 'cincinnati'

    },

    {
        'first_name': 'brian',
        'last_name': 'mochtyak',
        'age': 27,
        'city': 'covington'

    },

    {
        'first_name': 'evan',
        'last_name': 'horvath',
        'age': 27,
        'city': 'chicago'

    }
]

# LOOP THROUGH THE LIST AND PRINT EVERYTHING ABOUT EACH PERSON
for person in people:
    print(f"\n{person['first_name'].title()} {person['last_name'].title()} is {person['age']} years old and lives in {person['city'].title()}")