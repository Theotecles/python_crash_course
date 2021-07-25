# START WITH USERS THAT NEED TO BE VERIFIED
# AND AN EMPTY LIST TO HOLD CONFIRMED USERS
uncomfirmed_users =[
    'alice',
    'brian',
    'candace'
]
confirmed_users = []

# VERIFY EACH USER UNTIL THERE ARE NO MORE UNCOMFIRMED USERS
#  MOVE EACH VERIFIED USER INTO THE LIST OF CONFIRMED USERS
while uncomfirmed_users:
    current_user = uncomfirmed_users.pop()

    print(f"verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# DISPLAY ALL CONFIRMED USERS
print("\nThe follwing users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())