# CREATE A DICTIONARY OF THREE RIVERS
rivers = {
    'ohio': 'usa',
    'seine': 'france',
    'nile': 'egypt'
}

# CREATE A LOOP THAT RUNS THROUGH IT AND PRINTS A LITTLE BLURB
for i, y in rivers.items():
    print(f"{i.title()} runs through the country {y.title()}.\n")

# CREATE LOOP THAT JUST PRINTS THE KEYS
for i in rivers:
    print(i.title())

# CREATE A LOOP THAT JUST PRINTS THE TERMS
for i in rivers.values():
    print(i.title())