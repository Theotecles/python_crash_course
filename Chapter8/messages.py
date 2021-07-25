# MAKE A LIST OF SHORT TEXT MESSAGES
messages = [
    'lol',
    'lmao',
    'rofl',
    'wya'
]

# CREATE A FUNCTION THAT PRINTS EACH TEXT MESSAGE INDIVIDUALLY
def show_messages(messages):
    """ PRINT EACH MESSAGE """
    for message in messages:
        print(message)

# CALL THE FUNTION ON MESSAGES
show_messages(messages)

# CREATE A NEW FUNTION THAT PRINTS EACH MESSAGE AND SENDS IT TO A NEW LIST SENT_MESSAGES
def send_messages(unsent_messages, sent_messages):
    """
    PRINT EACH MESSAGE AND PUT THEM IN THE
    SENT MESSAGES LIST
    """
    while unsent_messages:
        print("Sending text message...")
        message = unsent_messages.pop()
        print(message)
        sent_messages.append(message)

unsent_messages = [
    'lol',
    'lmao',
    'rofl',
    'wya'
]
sent_messages = []

send_messages(unsent_messages, sent_messages)

print(unsent_messages)
print(sent_messages)

# REDO THE SAME THING BUT KEEP BOTH LISS IN TACT
unsent_messages = [
    'lol',
    'lmao',
    'rofl',
    'wya'
]
sent_messages = []

send_messages(unsent_messages[:], sent_messages)

print(unsent_messages)
print(sent_messages)