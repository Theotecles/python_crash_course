# CREATE SEVERAL DICTIONARIES OF PETS
pet1 = {
    'name': 'reggie',
    'owner': 'brian',
    'animal': 'dog'
}

pet2 = {
    'name': 'frankie',
    'owner': 'liz',
    'animal': 'dog'
}

pet3 = {
    'name': 'larry',
    'owner': 'pardon',
    'animal': 'goldfish'
}

pets = [
    pet1,
    pet2,
    pet3
]

# USE A FOR LOOP TO PRINT EVERYTHING I KNOW ABOUT EACH PET
for pet in pets:
    print(f"{pet['name'].title()} is a {pet['animal']} who is taken care of by {pet['owner'].title()}.")