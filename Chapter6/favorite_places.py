# CREATE A LIST OF PEOPLE AND THEIR FAVORITE PLACES
favorite_places = {
    'brian': ['delgardo', 'bdubs'],
    'shauna': ['delgardo', 'mizunte'],
    'evan': ['sidebar']
}

# LOOP THROUGH THE DICTIONARY FOR EACH PERSON AND SAY THEIR FAVORITE PLACES
for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}'s favorite places are:")
    else:
        print(f"\n{name.title()}'s favorite place is:")
    for place in places:
        print(f"{place.title()}")