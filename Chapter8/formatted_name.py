# CREATE A FUNCTION CALLED GET_FORMATTED_NAME
def get_formatted_name(first_name, last_name):
    """RETURN A FULL NAME, NEATLY FORMATTED."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# CHANGE GET_FORMATTED_NAME SO IT TAKES MIDDLE NAMES INTO ACCOUNT
def get_formatted_name(first_name, last_name, middle_name=''):
    """RETURN A FULL NAME, NEATLY FORMATTED"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# USE A WHILE LOOP TO KEEP ASKING FOR MORE NAMES
def get_formatted_name(first_name, last_name):
    """RETURN A FULL NAME, NEATLY FORMATTED."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")