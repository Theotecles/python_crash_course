# USE A CONDITIONAL STATEMENT
prompt = "\nWhat is your age? "
prompt += "\n(Enter 'quit' to proceed to payment.) "
    
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        age = int(message)
        if age < 3:
            cost = 0
        elif age <= 12:
            cost  = 10
        else:
            cost = 15

        print(f"The cost of the movie ticket is ${cost}.")
    else:
        print("Please proceed to payment.")