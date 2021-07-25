# CREATEA A LIST OF BANNED USERS

banned_users = [
    'andrew',
    'carolina',
    'david'
]

# USE AN IF STATEMENT TO SEE IF A USER IS IN THE BANNED LIST

user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")