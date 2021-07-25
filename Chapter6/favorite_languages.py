# CREATE A LIST OF FAVORITE LANGUAGES
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# LOOP THROUGH THE DICTIONARY AND PRINT EVERYONE'S FAVORITE LANGUAGE
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# LOOP THROUGH ALL THE KEYS IN THE DICTIONARY
for name in favorite_languages.keys():
    print(name.title())

# LOOPING THROUGH KEYS IS THE DEFAULT SO YOU CAN ACCOMPLISH THE SAME THING WITH THE FOLLOWING CODE
for name in favorite_languages:
    print(name.title())

# CREATEA A LOP THAT WRITES A MESSAGE TO FRIENDS AND IF THEY ARE IN THE LIST
# ACKNOWLEDGE THEIR FAVORITE LANGUAGE
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# USE KEYS METHOD TO SEE IF SOMETHING IS IN THE DICTIONARY OR NOT
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# SORT THE KEYS IN ALPHABETICAL ORDER BEFORE LOOPING THROUGH THEM
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking our poll.")

# LOOP THROUGH JUST VALUES
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# ONLY PRINT UNIQUE VALUES
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# CREATE A DICTIONARY OF EACH PERSONS' FAVORITE LANAGUAGES
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# PRINT EACH PERSONS' NAME AND THEIR FAVORITE LANGUAGE(S)
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    else:
        print(f"\n{name.title()}'s favorite language is:")
    for language in languages:
        print(f"\t{language.title()}")