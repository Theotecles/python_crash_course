# USE AN ACTIVE VARIABLE TO END THE LOOP
prompt = "\nWhat is your age? "
prompt += "\n(Enter 'quit' to proceed to payment.) "

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:        
        age = int(age)
        if age < 3:
            cost = 0
        elif age <= 12:
            cost  = 10
        else:
            cost = 15

        print(f"The cost of the movie ticket is ${cost}.")