# CREATE A LOOP THAT ASKS THE USER THEIR AGE AND TELLS
# THEM THE COST OF THE TICKET DEPENDING ON THEIR AGE
prompt = "What is your age? "

while True:
    age = int(input(prompt))

    if age < 3:
        cost = 0
    elif age <= 12:
        cost  = 10
    else:
        cost = 15

    print(f"The cost of the movie ticket is ${cost}.")