# CREATE AN EMPTY DICTIONARY FOR RESPONSES
responses = {}

# SET A POLLING FLAG EQUAL TO TRUE
polling_active = True

# CREATE A FOR LOOP THAT ASKS FOR RESPONSES FROM THE SURVEY
while polling_active:
    # PROMPT THE PERSON FOR THEIR NAME AND RESPONSE
    name = input("\nWhat is your name? ")
    response = input("\nWhat is your dream vacation? ")

    # STORE THE RESPONSE IN THE DICTIONARY
    responses[name] = response

    # ASK IF ANYONE ELSE WOULD LIKE TO TAKE THE POLL
    repeat = input("Would anyone else like to take the poll? ")
    if repeat == 'no':
        polling_active = False

# POLLING IS COMPLETE PRINT THE RESULTS
print("--- Displaying Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to take a dream vacation to {response.title()}.")