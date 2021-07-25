# WRITE A SIMPLE PROMPT ASKING THE USER FOR THEIR NAME
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# WRITE A NEW PROMPT WITH MORE THAN ONE LINE
prompt = "If you tell us who you are, we can personilze the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# ASK ANOTHER QUESTION ABOUT THE PERSON'S AGE AND SEE IF IT IS OLDER THAN 18
age = input("How old are you? ")
age = int(age)
age >= 18