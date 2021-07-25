# CREATE A FUNCTIONCALLED BUILD_PERSON
def build_person(first_name, last_name):
    """RETURN A DICTIONARY OF INFORMATION ABOUT THE PERSON"""
    person = {
        'first': first_name,
        'last': last_name
        }
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# MODIFY BUILD_PERSON SO IT TAKES INTO ACCOUNT A PERSON'S AGE
def build_person(first_name, last_name, age=None):
    """RETURN A DICTIONARY OF INFORMATION ABOUT THE PERSON"""
    person = {
        'first': first_name,
        'last': last_name
        }
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)