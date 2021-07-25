# CREATE A LIST OF FAVORITE LANGUAGES
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# LIST OF PEOPLE WHO SHOULD TAKE THE POLL
people = [
    'brian',
    'jen',
    'shauna',
    'phil',
    'evan'    
]

# LOOP THROUGH THE LIST AND WRITE A MESSAGE TO THEM BASED OFF WHETHER OR NOT THEY HAVE TAKEN THE POLL
for name in people:
    if name in favorite_languages.keys():
        print(f"Hello, {name.title()} thank you for taking the survey!\n")
    else:
        print(f"Hello, {name.title()} please take the survey. We would really appreciate it!\n")