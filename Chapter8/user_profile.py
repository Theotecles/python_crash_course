# CREATE A FUNCTION CALLED BUILD_PROFILE
def build_profile(first, last, **user_info):
    """BUILD A DICTIONARY CONTAINING EVERYTHING WE KNOW ABOUT A USER"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert',
                             'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

user_profile = build_profile('brian',
                             'mochtyak',
                             location='cincinnati',
                             hobby='golf',
                             goal='python masta')

print(user_profile)