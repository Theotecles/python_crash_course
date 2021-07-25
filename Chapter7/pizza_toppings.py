# WRITE A WHILE LOOP THAT PROMPTS THE USER FOR PIZZA TOPPINGS
prompt = "\nWhat topping(s) would you like on your pizza? "
prompt += "\n(Enter 'quit' when you are done adding toppings to your pizza)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping.title()} to your pizza...")