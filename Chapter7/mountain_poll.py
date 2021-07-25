# CREATE A WHILE LOOP THAT ASKS FOR MULTIPLE USER INPUT
responses = {}

# SET A FLAG TO INDICATE THAT POLLING IS ACTIVE
polling_active = True

while polling_active:
    # PROMPT FPR THE PERSON'S NAME AND RESPONSE
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climp some day? ")

    # STORE THE RESPONSE IN THE DICTIONARY
    responses[name] = response

    # FIND OUT IF ANYONE ELSE IS GOING TO TAKE THE POLL
    repeat = input("Would you like to let another person respond?: (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# POLLING IS COMPLETE SHOW THE RESULTS
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")