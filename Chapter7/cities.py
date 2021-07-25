# CREATE A PROMPT THAT ASKS SOMEONE FOR A CITY THEY HAVE VISITED
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.}"

# USE A BREAK STAEMENT TO END THE WHILE LOOP
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")