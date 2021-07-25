# USE AN INPUT MESSAGE TO ASK THE USER SOMETHING
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# MODIFY THE ABOVE SO THE USER HAS CONTROL TO END THE PROGRAM
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# MODIFY THE WHILE LOOP SO IT HAS A FLAG
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)