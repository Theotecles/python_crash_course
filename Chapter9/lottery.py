import random

numbers_letters = [
    '69',
    '13',
    '22',
    '17',
    '44',
    '64',
    '87',
    '98',
    '12',
    '47',
    's',
    'b',
    't',
    'l',
    'g'
]

print(random.choice(numbers_letters))
print(random.choice(numbers_letters))
print(random.choice(numbers_letters))
print(random.choice(numbers_letters))

my_number = ['98', 'l', '47', 'g']

pulling_numbers = True

numbers_pulled = []
total_pulls = []

while pulling_numbers:
    pulled_number = random.choice(numbers_letters)
    numbers_pulled.append(pulled_number)
    total_pulls.append(numbers_pulled)

    if len(numbers_pulled) == 4:

        if numbers_pulled == my_number:
            pulling_numbers = False
            print(numbers_pulled)
        else:
            pulling_numbers = True
            numbers_pulled = []

print(f"It took {len(total_pulls)} numbers to get to your number!")

print(numbers_pulled)